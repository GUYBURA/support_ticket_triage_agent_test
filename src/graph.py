from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from src.nodes.classify import classify
from src.nodes.extract import extract
from src.nodes.ticket_summary import ticket_summary
from src.nodes.decision import decide
from src.nodes.escalate import escalate
from src.nodes.specialist import specialist
from src.nodes.auto_respond import auto_respond
from src.state import State

def route(state:State) -> str:
    return state["decision"].action

tools = []

support_agent = StateGraph(State)
support_agent.add_node("classify", classify)
support_agent.add_node("extract", extract)
support_agent.add_node("tools", ToolNode(tools))
support_agent.add_node("ticket_summary", ticket_summary)
support_agent.add_node("decide", decide)
support_agent.add_node("escalate", escalate)
support_agent.add_node("specialist", specialist)
support_agent.add_node("auto_respond", auto_respond)

support_agent.add_edge(START, "classify")
support_agent.add_edge("classify", "extract")
support_agent.add_conditional_edges(
    "extract", tools_condition, {"tools": "tools", END: "ticket_summary"}
)
support_agent.add_edge("tools", "ticket_summary")
support_agent.add_edge("ticket_summary", "decide")
support_agent.add_conditional_edges(
    "decide", 
    route,
    {
        "escalate_to_human": "escalate",
        "route_to_specialist": "specialist",
        "auto_respond": "auto_respond"
    }
)
support_agent.add_edge("escalate", END)
support_agent.add_edge("specialist", END)
support_agent.add_edge("auto_respond", END)

graph = support_agent.compile()