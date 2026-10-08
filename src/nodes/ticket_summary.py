from langchain.messages import HumanMessage, SystemMessage
from src.state import State
from src.config import get_llm
from src.prompts.prompts import TICKET_SUMMARY_PROMPT
from src.prompts.format import format_ticket
from src.tools import tools

def ticket_summary(state:State) -> dict:
    llm = get_llm().bind_tools(tools)
    
    if not state.get("messages"):
        human = HumanMessage(content=(
            f"{format_ticket(state['ticket'])}\n\n"
            f"Ticket urgency: {state['ticket_urgency'].urgency}\n"
            f"Product: {state['key_information'].product}\n"
            f"Issue type: {state['key_information'].issue_type}\n"
            f"Customer sentiment: {state['key_information'].customer_sentiment}"
        ))
        response = llm.invoke([
            SystemMessage(content=TICKET_SUMMARY_PROMPT),
            human
        ])
        new_messages = [human, response]
    else:
        response = llm.invoke([SystemMessage(content=TICKET_SUMMARY_PROMPT)] + state["messages"])
        new_messages = [response]
    
    update = {"messages": new_messages}
    if not response.tool_calls:
        update["summary"] = response.text
    return update
