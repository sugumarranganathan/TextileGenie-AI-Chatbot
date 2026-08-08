# ==========================================================
# TEXTILEGENIE AI CHATBOT
# LANGGRAPH WORKFLOW
# ==========================================================

from langgraph.graph import StateGraph, END

from agents.state import TextileState

from agents.query_agent import query_agent
from agents.supervisor_agent import supervisor_agent
from agents.sales_agent import sales_agent
from agents.inventory_agent import inventory_agent
from agents.purchase_agent import purchase_agent
from agents.trend_agent import trend_agent
from agents.forecast_agent import forecast_agent
from agents.insight_agent import insight_agent
from agents.recommendation_agent import recommendation_agent
from agents.validation_agent import validation_agent


# ==========================================================
# BUILD TEXTILEGENIE WORKFLOW
# ==========================================================

def build_graph():

    workflow = StateGraph(TextileState)

    # ------------------------------------------------------
    # ADD AGENTS
    # ------------------------------------------------------

    workflow.add_node(
        "query",
        query_agent
    )

    workflow.add_node(
        "supervisor",
        supervisor_agent
    )

    workflow.add_node(
        "sales",
        sales_agent
    )

    workflow.add_node(
        "inventory",
        inventory_agent
    )

    workflow.add_node(
        "purchase",
        purchase_agent
    )

    workflow.add_node(
        "trend",
        trend_agent
    )

    workflow.add_node(
        "forecast",
        forecast_agent
    )

    workflow.add_node(
        "insight",
        insight_agent
    )

    workflow.add_node(
        "recommendation",
        recommendation_agent
    )

    workflow.add_node(
        "validation",
        validation_agent
    )

    # ------------------------------------------------------
    # START
    # ------------------------------------------------------

    workflow.set_entry_point(
        "query"
    )

    # ------------------------------------------------------
    # AGENT CONNECTIONS
    # ------------------------------------------------------

    workflow.add_edge(
        "query",
        "supervisor"
    )

    workflow.add_edge(
        "supervisor",
        "sales"
    )

    workflow.add_edge(
        "sales",
        "inventory"
    )

    workflow.add_edge(
        "inventory",
        "purchase"
    )

    workflow.add_edge(
        "purchase",
        "trend"
    )

    workflow.add_edge(
        "trend",
        "forecast"
    )

    workflow.add_edge(
        "forecast",
        "insight"
    )

    workflow.add_edge(
        "insight",
        "recommendation"
    )

    workflow.add_edge(
        "recommendation",
        "validation"
    )

    # ------------------------------------------------------
    # FINAL
    # ------------------------------------------------------

    workflow.add_edge(
        "validation",
        END
    )

    # ------------------------------------------------------
    # COMPILE
    # ------------------------------------------------------

    return workflow.compile()
