import json
import sys
from src.graph import graph

def main() -> None:
    sys.stdout.reconfigure(encoding='utf-8')
    
    path = sys.argv[1] if len(sys.argv) > 1 else "data/ticket.json"
    with open(path, "r", encoding="utf-8") as f:
        tickets = json.load(f)
    
    for ticket in tickets:
        print(f"\n=== {ticket['ticket_id']} ===")
        try:
            for step in graph.stream({"ticket": ticket}, stream_mode="updates"):
                for node, update in step.items():
                    print(f"{node}")
                    if node == "classify":
                        print(f"  urgency: {update['ticket_urgency'].urgency}")
                    elif node == "extract":
                        k = update["key_information"]
                        print(f"  product: {k.product} | issue: {k.issue_type} | sentiment: {k.customer_sentiment}")
                    elif node == "ticket_summary":
                        for m in update["messages"]:
                            if m.type == "ai" and m.tool_calls:
                                for call in m.tool_calls:
                                    print(f"  tool call: {call['name']} ({call['args']})")
                        if "summary" in update:
                            print(f"  summary: {update['summary']}")
                    elif node == "tools":
                        for m in update["messages"]:
                            print(f"  tool result ({m.name}): {m.text[:80]}")
                    elif node == "decide":
                        print(f"  action: {update['decision'].action}")
                    elif node in ("escalate", "specialist"):
                        print(f"  handoff_note: {update['handoff_note']}")
                    elif node == "auto_respond":
                        print(f"  reply: {update['customer_reply']}")
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            continue
        
if __name__ == "__main__":
    main()