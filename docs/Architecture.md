## Architecture of This Project
1. **UV** (Used to set up Python projects. Fast and easy to use.)
2. **LangChain** (Used to develop agents, tools, and structured outputs.)
3. **LangGraph** (Used to create workflows for agents, e.g., decision-making.)
4. **LangSmith** (Used for evaluation, observability, and logging. It integrates well with the LangChain and LangGraph ecosystem.)

## Folder Structure

```text
support_ticket_triage_agent_test/
├── data/               # Example data and the knowledge base
├── docs/               # Project documentation
└── src/                # Source code
    ├── nodes/          # Nodes for the graph workflow
    ├── prompts/        # Prompts for the LLM
    └── tools/          # Tools for the LLM
```