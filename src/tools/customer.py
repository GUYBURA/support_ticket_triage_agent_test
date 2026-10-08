import json
from pathlib import Path
from langchain.tools import tool

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "customer_information.json"

def _load_customer() -> dict[str,str]:
    with open(DATA_PATH, encoding="utf-8") as f:
        return {c["customer_id"]: c["information"] for c in json.load(f)}

@tool
def check_customer_information(customer_id: str) -> str:
    """This tool checks the customer information
    
    Args:
        customer_id (str): The unique identifier of the customer. e.g. 'C-000'

    """
    info = _load_customer().get(customer_id)
    if info is None:
        return f"No information found for customer ID '{customer_id}'."
    return info