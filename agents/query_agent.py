# ==========================================================
# TEXTILEGENIE AI CHATBOT
# QUERY UNDERSTANDING AGENT
# ==========================================================

import re


class QueryUnderstandingAgent:

    def __init__(self):

        self.name = "Query Understanding Agent"


    # ======================================================
    # MAIN METHOD
    # ======================================================

    def run(self, question: str):

        # --------------------------------------------------
        # CLEAN QUESTION
        # --------------------------------------------------

        q = question.lower().strip()


        # --------------------------------------------------
        # PERIOD DETECTION
        # --------------------------------------------------

        period_days = 30

        match = re.search(
            r"last\s+(\d+)\s+days?",
            q
        )

        if match:

            period_days = int(
                match.group(1)
            )

        elif "yesterday" in q:

            period_days = 1

        elif (
            "last week" in q
            or "past week" in q
        ):

            period_days = 7

        elif (
            "last month" in q
            or "past month" in q
        ):

            period_days = 30


        # --------------------------------------------------
        # CATEGORY DETECTION
        # --------------------------------------------------

        category = ""

        category_map = {

            "shirts": "Shirt",
            "shirt": "Shirt",

            "t-shirts": "T-Shirt",
            "t-shirt": "T-Shirt",

            "jeans": "Jeans",
            "jean": "Jeans",

            "pants": "Pant",
            "pant": "Pant",

            "kurtis": "Kurti",
            "kurti": "Kurti",

            "sarees": "Saree",
            "saree": "Saree",

            "dresses": "Dress",
            "dress": "Dress"
        }


        for keyword, value in category_map.items():

            if keyword in q:

                category = value

                break


        # --------------------------------------------------
        # INTENT DETECTION
        # --------------------------------------------------

        # UNSOLD PRODUCTS

        if (

            "not sold" in q

            or "zero sales" in q

            or "no sales" in q

            or "didn't sell" in q

            or "did not sell" in q

            or "unsold" in q

        ):

            intent = "unsold_products"


        # FAST MOVING

        elif (

            "fastest" in q

            or "fast moving" in q

            or "fast-moving" in q

            or "moved fast" in q

            or "best selling" in q

            or "best-selling" in q

            or "top selling" in q

            or "top-selling" in q

        ):

            intent = "fast_moving"


        # SLOW MOVING

        elif (

            "slow moving" in q

            or "slow-moving" in q

            or "slow seller" in q
            or "slow sellers" in q

        ):

            intent = "slow_moving"


        # LOW STOCK

        elif (

            "low stock" in q

            or "running low" in q

            or "low inventory" in q

            or "stock is low" in q

        ):

            intent = "low_stock"


        # PURCHASE / REORDER

        elif (

            "order" in q

            or "purchase" in q

            or "buy" in q

            or "reorder" in q

            or "restock" in q

            or "replenish" in q

        ):

            intent = "purchase_recommendation"


        # TREND

        elif (

            "growing" in q

            or "growth" in q

            or "declining" in q

            or "decline" in q

            or "trend" in q

            or "trending" in q

        ):

            intent = "trend"


        # INVENTORY

        elif (

            "inventory" in q

            or "stock" in q
            or "available stock" in q

        ):

            intent = "inventory"


        # BRAND SALES

        elif (

            "brand" in q

            or "brands" in q

        ):

            intent = "brand_sales"


        # GENERAL SALES

        else:

            intent = "sales_summary"


        # --------------------------------------------------
        # METRIC DETECTION
        # --------------------------------------------------

        if (

            "revenue" in q

            or "sales value" in q

            or "sales amount" in q

            or "turnover" in q

        ):

            metric = "revenue"


        elif "profit" in q:

            metric = "profit"


        elif (

            "quantity" in q

            or "units" in q

            or "pieces" in q

            or "number sold" in q

        ):

            metric = "units"


        else:

            metric = "units"


        # --------------------------------------------------
        # BRAND DETECTION
        # --------------------------------------------------

        brand = ""

        brands = [

            "Peter England",

            "Van Heusen",

            "Louis Philippe",

            "Allen Solly",

            "Raymond",

            "Levis",

            "U.S. Polo",

            "Park Avenue"
        ]


        for item in brands:

            if item.lower() in q:

                brand = item

                break


        # --------------------------------------------------
        # RETURN STRUCTURED RESULT
        # --------------------------------------------------

        return {

            "intent": intent,

            "category": category,

            "brand": brand,

            "period_days": period_days,

            "metric": metric,

            "question": question
        }
