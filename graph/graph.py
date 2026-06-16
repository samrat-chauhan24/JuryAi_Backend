from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.state import LegalState

from graph.nodes.validator import (
    validator_node
)

from graph.nodes.router import (
    router_node
)

from graph.nodes.rag import (
    rag_node
)

from graph.nodes.llm import (
    llm_node
)

from graph.nodes.formatter import (
    formatter_node
)

builder = StateGraph(
    LegalState
)

# Nodes
builder.add_node(
    "validator",
    validator_node
)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "llm",
    llm_node
)

builder.add_node(
    "formatter",
    formatter_node
)

# Edges
builder.add_edge(
    START,
    "validator"
)

builder.add_edge(
    "validator",
    "router"
)

builder.add_edge(
    "router",
    "rag"
)

builder.add_edge(
    "rag",
    "llm"
)

builder.add_edge(
    "llm",
    "formatter"
)

builder.add_edge(
    "formatter",
    END
)

graph = builder.compile()