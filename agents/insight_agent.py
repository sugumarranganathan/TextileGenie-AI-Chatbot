class InsightAgent:

    def __init__(self):
        self.name = "Business Insight Agent"

    def run(self, state):

        insights = []

        analysis = state.get(
            "analysis",
            {}
        )

        trend = state.get(
            "trend"
        )

        inventory = state.get(
            "inventory_result"
        )

        # Sales insight
        total_units = analysis.get(
            "total_units",
            0
        )

        total_revenue = analysis.get(
            "total_revenue",
            0
        )

        insights.append(
            f"Total recent sales movement: "
            f"{total_units:,} units."
        )

        insights.append(
            f"Recent sales revenue: "
            f"₹{total_revenue:,.0f}."
        )

        # Fastest brand
        brand_sales = analysis.get(
            "brand_sales"
        )

        if (
            brand_sales is not None
            and not brand_sales.empty
        ):

            top = brand_sales.iloc[0]

            insights.append(
                f"{top['Brand']} is the "
                f"fastest-moving brand with "
                f"{int(top['Quantity'])} units."
            )

        # Inventory insight
        if inventory is not None:

            low_stock = inventory[
                inventory["Low_Stock"]
            ]

            if len(low_stock) > 0:

                insights.append(
                    f"{len(low_stock)} products "
                    f"need stock review."
                )

        # Trend insight
        if (
            trend is not None
            and not trend.empty
        ):

            top_growth = trend.iloc[0]

            insights.append(
                f"{top_growth['Brand']} shows "
                f"{top_growth['Growth_%']}% "
                f"brand movement change."
            )

        return insights
