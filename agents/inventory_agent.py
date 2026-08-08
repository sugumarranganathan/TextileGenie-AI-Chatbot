import pandas as pd


class InventoryAgent:

    def __init__(self):
        self.name = "Inventory Analysis Agent"

    def run(self, state):

        inventory = state[
            "inventory_df"
        ].copy()

        sales = state[
            "sales_df"
        ].copy()

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

        if category:

            inventory = inventory[
                inventory["Category"]
                .astype(str)
                .str.lower()
                .str.contains(
                    category.lower(),
                    na=False
                )
            ]

        sold = (
            recent_sales
            .groupby("Product_ID")["Quantity"]
            .sum()
            .reset_index(
                name="Units_Sold"
            )
        )

        result = inventory.merge(
            sold,
            on="Product_ID",
            how="left"
        )

        result["Units_Sold"] = (
            result["Units_Sold"]
            .fillna(0)
        )

        result["Daily_Sales"] = (
            result["Units_Sold"]
            / period_days
        )

        result["Days_of_Stock"] = result.apply(
            lambda row:
                (
                    row["Current_Stock"]
                    /
                    row["Daily_Sales"]
                )
                if row["Daily_Sales"] > 0
                else 999,
            axis=1
        )

        result["Stock_Value"] = (
            result["Current_Stock"]
            *
            result["Purchase_Price"]
        )

        result["Low_Stock"] = (
            result["Days_of_Stock"] < 14
        )

        return result
