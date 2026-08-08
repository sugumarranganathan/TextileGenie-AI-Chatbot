# ==========================================================
# TEXTILEGENIE AI CHATBOT
# LANGGRAPH WORKFLOW
# ==========================================================

from langgraph.graph import StateGraph, END

from agents.state import TextileState

from agents.query_agent import QueryUnderstandingAgent
from agents.supervisor_agent import SupervisorAgent
from agents.sales_agent import SalesAgent
from agents.inventory_agent import InventoryAgent
from agents.purchase_agent import PurchaseAgent
from agents.trend_agent import TrendAgent
from agents.forecast_agent import ForecastAgent
from agents.insight_agent import InsightAgent
from agents.recommendation_agent import RecommendationAgent
from agents.validation_agent import ValidationAgent


# ==========================================================
# CREATE AGENT OBJECTS
# ==========================================================

query_agent = QueryUnderstandingAgent()

supervisor_agent = SupervisorAgent()

sales_agent = SalesAgent()

inventory_agent = InventoryAgent()

purchase_agent = PurchaseAgent()

trend_agent = TrendAgent()

forecast_agent = ForecastAgent()

insight_agent = InsightAgent()

recommendation_agent = RecommendationAgent()

validation_agent = ValidationAgent()


# ==========================================================
# LANGGRAPH NODE FUNCTIONS
# ==========================================================

def query_node(state: TextileState):

    result = query_agent.run(
        state["question"]
    )

    return result


def supervisor_node(state: TextileState):

    result = supervisor_agent.run(
        state
    )

    return result


def sales_node(state: TextileState):

    result = sales_agent.run(
        state
    )

    return result


def inventory_node(state: TextileState):

    result = inventory_agent.run(
        state
    )

    return result


def purchase_node(state: TextileState):

    result = purchase_agent.run(
        state
    )

    return result


def trend_node(state: TextileState):

    result = trend_agent.run(
        state
    )

    return result


def forecast_node(state: TextileState):

    result = forecast_agent.run(
        state
    )

    return result


def insight_node(state: TextileState):

    result = insight_agent.run(
        state
    )

    return result


def recommendation_node(state: TextileState):

    result = recommendation_agent.run(
        state
    )

    return result


def validation_node(state: TextileState):

    result = validation_agent.run(
        state
    )

    return result


# ==========================================================
# BUILD TEXTILEGENIE WORKFLOW
# ==========================================================

def build_graph():

    workflow = StateGraph(
        TextileState
    )


    # ======================================================
    # ADD NODES
    # ======================================================

    workflow.add_node(
        "query",
        query_node
    )

    workflow.add_node(
        "supervisor",
        supervisor_node
    )

    workflow.add_node(
        "sales",
        sales_node
    )

    workflow.add_node(
        "inventory",
        inventory_node
    )

    workflow.add_node(
        "purchase",
        purchase_node
    )

    workflow.add_node(
        "trend",
        trend_node
    )

    workflow.add_node(
        "forecast",
        forecast_node
    )

    workflow.add_node(
        "insight",
        insight_node
    )

    workflow.add_node(
        "recommendation",
        recommendation_node
    )

    workflow.add_node(
        "validation",
        validation_node
    )


    # ======================================================
    # START
    # ======================================================

    workflow.set_entry_point(
        "query"
    )


    # ======================================================
    # WORKFLOW CONNECTIONS
    # ======================================================

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


    # ======================================================
    # END
    # ======================================================

    workflow.add_edge(
        "validation",
        END
    )


    # ======================================================
    # COMPILE
    # ======================================================

    return workflow.compile()
