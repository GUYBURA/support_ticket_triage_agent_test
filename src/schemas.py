from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    sent_at: str = Field(description="Relative time the message was sent, e.g. '3 hrs ago'.")
    content: str = Field(description="Text of the customer message.")


class Ticket(BaseModel):
    ticket_id: str = Field(description="Unique ticket identifier.")
    customer_id: str = Field(description="Unique customer identifier.")
    messages: list[Message] = Field(description="Customer messages in the ticket, oldest first.")


class TicketUrgency(BaseModel):
    reasoning: str = Field(
        description="Brief explanation of why this urgency level fits, based on the ticket content."
    )
    urgency: Literal["Critical", "High", "Medium", "Low"] = Field(
        description=(
            "Urgency level of the ticket, based on the content and context."
        )
    )


class KeyInformation(BaseModel):
    product: str = Field(description="Product or feature the customer is asking about.")
    issue_type: str = Field(
        description="Short category of the problem, e.g. 'login failure', 'billing error', 'bug report'."
    )
    customer_sentiment: Literal["Positive", "Neutral", "Negative"] = Field(
        description="Overall tone of the customer. Negative includes frustrated or angry."
    )


class Decision(BaseModel):
    reasoning: str = Field(
        description="Brief explanation of why this action was chosen, given urgency and key information."
    )
    action: Literal["escalate_to_human", "route_to_specialist", "auto_respond"] = Field(
        description=(
            "action to take on the ticket, based on urgency and key information. "
        )
    )


class TicketSummary(BaseModel):
    summary: str = Field(description="One or two sentence summary of the customer's issue.")
