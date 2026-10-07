from src.schemas import Ticket

def format_ticket(ticket: Ticket) -> str:
    ticket = Ticket.model_validate(ticket)
    lines = [f"Ticket ID: {ticket.ticket_id} Customer ID: {ticket.customer_id}"]
    for i, m in enumerate(ticket.messages, start=1):
        lines.append(f"Message {i} ({m.sent_at}): {m.content}")
    return "\n".join(lines)