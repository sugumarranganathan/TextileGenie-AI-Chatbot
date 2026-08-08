import pandas as pd


class TrendAgent:

    def __init__(self):
        self.name = "Trend Analysis Agent"

    def run(self, state):

        sales = state[
            "sales_df"
        ].copy()

        sales["Date"] = pd.to_datetime(
            sales["Date"]
        )

        latest_date = sales["Date"].max()

        recent_start = (
            latest_date
            - pd.Timedelta(days=14)
        )

        previous_start = (
            latest_date
            - pd.Timedelta(days=29)
        )

        recent = sales[
            sales["Date"] >= recent_start
        ]

        previous = sales[
            (
                sales["Date"] >= previous_start
            )
            &
            (
                sales["Date"] < recent_start
            )
        ]

        recent_brand = (
            recent
            .groupby("Brand")["Quantity"]
            .sum()
        )

        previous_brand = (
            previous
            .groupby("Brand")["Quantity"]
            .sum()
        )

        records = []

        for brand, recent_units in recent_brand.items():

            previous_units = (
                previous_brand
                .get(brand, 0)
            )

            if previous_units == 0:

                growth = 100.0

            else:

                growth = (
                    (
                        recent_units
                        -
                        previous_units
                    )
                    /
                    previous_units
                ) * 100

            records.append({
                "Brand": brand,
                "Recent_Units": int(
                    recent_units
                ),
                "Previous_Units": int(
                    previous_units
                ),
                "Growth_%": round(
                    growth,
                    2
                )
            })

        trend_df = pd.DataFrame(
            records
        )

        if not trend_df.empty:

            trend_df = trend_df.sort_values(
                "Growth_%",
                ascending=False
            )

        return trend_df
