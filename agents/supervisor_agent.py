from agents.query_agent import QueryUnderstandingAgent
from agents.sales_agent import SalesAgent
from agents.inventory_agent import InventoryAgent
from agents.purchase_agent import PurchaseAgent
from agents.trend_agent import TrendAgent
from agents.forecast_agent import ForecastAgent
from agents.insight_agent import InsightAgent
from agents.recommendation_agent import RecommendationAgent
from agents.validation_agent import ValidationAgent


class SupervisorAgent:

    def __init__(self):

        self.query_agent = (
            QueryUnderstandingAgent()
        )

        self.sales_agent = (
            SalesAgent()
        )

        self.inventory_agent = (
            InventoryAgent()
        )

        self.purchase_agent = (
            PurchaseAgent()
        )

        self.trend_agent = (
            TrendAgent()
        )

        self.forecast_agent = (
            ForecastAgent()
        )

        self.insight_agent = (
            InsightAgent()
        )

        self.recommendation_agent = (
            RecommendationAgent()
        )

        self.validation_agent = (
            ValidationAgent()
        )

    def run(self, question, data):

        # =================================
        # 1. UNDERSTAND QUESTION
        # =================================

        query_result = (
            self.query_agent.run(
                question
            )
        )

        state = {

            "question": question,

            "products_df":
                data["products"],

            "sales_df":
                data["sales"],

            "inventory_df":
                data["inventory"],

            "purchase_df":
                data["purchase"],

            **query_result
        }

        # =================================
        # 2. SALES
        # =================================

        state["analysis"] = (
            self.sales_agent.run(
                state
            )
        )

        # =================================
        # 3. INVENTORY
        # =================================

        state[
            "inventory_result"
        ] = self.inventory_agent.run(
            state
        )

        # =================================
        # 4. PURCHASE
        # =================================

        state[
            "purchase_result"
        ] = self.purchase_agent.run(
            state
        )

        # =================================
        # 5. TREND
        # =================================

        state["trend"] = (
            self.trend_agent.run(
                state
            )
        )

        # =================================
        # 6. FORECAST
        # =================================

        state["forecast"] = (
            self.forecast_agent.run(
                state
            )
        )

        # =================================
        # 7. BUSINESS INSIGHTS
        # =================================

        state["insights"] = (
            self.insight_agent.run(
                state
            )
        )

        # =================================
        # 8. RECOMMENDATIONS
        # =================================

        state[
            "recommendations"
        ] = self.recommendation_agent.run(
            state
        )

        # =================================
        # 9. VALIDATION
        # =================================

        state[
            "validation"
        ] = self.validation_agent.run(
            state
        )

        return state
