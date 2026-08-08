import pandas as pd


class SalesAgent:

    def __init__(self):
        self.name = "Sales Analysis Agent"

    def run(self, state):

        sales = state["sales_df"].copy()

        period_days = state.get(
            "period_days",
            30
        )

        category = state.get(
            "category",
            ""
        )

        sales["Date"] = pd.to_datetime(
            sales["Date"]
        )

        latest_date = sales["Date"].max()

        start_date = (
            latest_date
            - pd.Timedelta(
                days=period_days - 1
            )
        )

        recent_sales = sales[
            sales["Date"] >= start_date
        ].copy()

        # Category filter
        if category:

            recent_sales = recent_sales[
                recent_sales["Category"]
                .astype(str)
                .str.lower()
                .str.contains(
                    category.lower(),
                    na=False
                )
            ]

        recent_sales["Revenue"] = (
            recent_sales["Quantity"]
            *
            recent_sales["Selling_Price"]
        )

        total_units = int(
            recent_sales["Quantity"].sum()
        )

        total_revenue = float(
            recent_sales["Revenue"].sum()
        )

        product_sales = (
            recent_sales
            .groupby(
                [
                    "Product_ID",
                    "Product_Name",
                    "Brand",
                    "Category"
                ]
            )["Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                "Quantity",
                ascending=False
            )
        )

        brand_sales = (
            recent_sales
            .groupby("Brand")["Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                "Quantity",
                ascending=False
            )
        )

        return {
            "period_sales": recent_sales,
            "total_units": total_units,
            "total_revenue": total_revenue,
            "product_sales": product_sales,
            "brand_sales": brand_sales
        }

