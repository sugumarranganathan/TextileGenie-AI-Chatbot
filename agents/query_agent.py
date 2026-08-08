import re


class QueryUnderstandingAgent:

    def __init__(self):
        self.name = "Query Understanding Agent"

    def run(self, question: str):

        q = question.lower().strip()

        # -----------------------------
        # PERIOD
        # -----------------------------

        period_days = 30

        match = re.search(
            r"last\s+(\d+)\s+days?",
            q
        )

        if match:
            period_days = int(match.group(1))

        elif "yesterday" in q:
            period_days = 1

        elif "last week" in q:
            period_days = 7

        elif "last month" in q:
            period_days = 30

        # -----------------------------
        # CATEGORY
        # -----------------------------

        category = ""

        categories = [
            "shirt",
            "shirts",
            "t-shirt",
            "t-shirts",
            "jeans",
            "jean",
            "pant",
            "pants",
            "kurti",
            "kurtis",
            "saree",
            "sarees",
            "dress",
            "dresses"
        ]

        for item in categories:

            if item in q:

                category = item.rstrip("s")
                break

        # -----------------------------
        # INTENT
        # -----------------------------

        if (
            "not sold" in q
            or "zero sales" in q
            or "no sales" in q
            or "didn't sell" in q
        ):

            intent = "unsold_products"

        elif (
            "fastest" in q
            or "fast moving" in q
            or "fast-moving" in q
            or "moved fast" in q
        ):

            intent = "fast_moving"

        elif (
            "slow moving" in q
            or "slow-moving" in q
        ):

            intent = "slow_moving"

        elif (
            "low stock" in q
            or "running low" in q
        ):

            intent = "low_stock"

        elif (
            "order" in q
            or "purchase" in q
            or "buy" in q
            or "reorder" in q
        ):

            intent = "purchase_recommendation"

        elif (
            "growing" in q
            or "growth" in q
            or "declining" in q
            or "trend" in q
        ):

            intent = "trend"

        elif "inventory" in q or "stock" in q:

            intent = "inventory"

        elif "brand" in q:

            intent = "brand_sales"

        else:

            intent = "sales_summary"

        # -----------------------------
        # METRIC
        # -----------------------------

        if (
            "revenue" in q
            or "sales value" in q
            or "sales amount" in q
        ):

            metric = "revenue"

        elif "profit" in q:

            metric = "profit"

        else:

            metric = "units"

        return {
            "intent": intent,
            "category": category,
            "period_days": period_days,
            "metric": metric
        }

