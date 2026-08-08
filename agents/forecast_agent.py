import pandas as pd


class ForecastAgent:

    def __init__(self):
        self.name = "Forecast Agent"

    def run(self, state):

        sales = state[
            "sales_df"
        ].copy()

        sales["Date"] = pd.to_datetime(
            sales["Date"]
        )

        daily_sales = (
            sales
            .groupby("Date")["Quantity"]
            .sum()
            .sort_index()
        )

        if daily_sales.empty:

            return {
                "daily_average": 0,
                "next_7_days": 0
            }

        recent_7 = daily_sales.tail(7)

        daily_average = float(
            recent_7.mean()
        )

        forecast_7_days = round(
            daily_average * 7
        )

        return {
            "daily_average": round(
                daily_average,
                2
            ),
            "next_7_days": forecast_7_days
        }
