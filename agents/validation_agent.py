import pandas as pd


class ValidationAgent:

    def __init__(self):
        self.name = "Validation & Metrics Agent"

    def run(self, state):

        sales = state[
            "sales_df"
        ].copy()

        inventory = state[
            "inventory_df"
        ].copy()

        products = state[
            "products_df"
        ].copy()

        checks = {}

        # -----------------------------
        # RECORD COUNTS
        # -----------------------------

        checks["sales_records"] = len(
            sales
        )

        checks["inventory_records"] = len(
            inventory
        )

        checks["product_records"] = len(
            products
        )

        # -----------------------------
        # MISSING IDS
        # -----------------------------

        checks[
            "missing_sales_product_ids"
        ] = int(
            sales["Product_ID"]
            .isna()
            .sum()
        )

        checks[
            "missing_inventory_product_ids"
        ] = int(
            inventory["Product_ID"]
            .isna()
            .sum()
        )

        # -----------------------------
        # DUPLICATES
        # -----------------------------

        checks[
            "duplicate_sales_records"
        ] = int(
            sales.duplicated().sum()
        )

        # -----------------------------
        # NEGATIVE VALUES
        # -----------------------------

        checks[
            "negative_sales_quantity"
        ] = int(
            (
                sales["Quantity"] < 0
            ).sum()
        )

        checks[
            "negative_inventory"
        ] = int(
            (
                inventory["Current_Stock"] < 0
            ).sum()
        )

        # -----------------------------
        # INVALID DATES
        # -----------------------------

        parsed_dates = pd.to_datetime(
            sales["Date"],
            errors="coerce"
        )

        checks[
            "invalid_sales_dates"
        ] = int(
            parsed_dates.isna().sum()
        )

        # -----------------------------
        # PRODUCT MATCHING
        # -----------------------------

        product_ids = set(
            products["Product_ID"]
        )

        sales_ids = set(
            sales["Product_ID"]
        )

        unmatched_sales = (
            sales_ids - product_ids
        )

        checks[
            "sales_products_not_in_master"
        ] = len(
            unmatched_sales
        )

        # -----------------------------
        # FINAL STATUS
        # -----------------------------

        problems = [
            checks[
                "missing_sales_product_ids"
            ],
            checks[
                "missing_inventory_product_ids"
            ],
            checks[
                "negative_sales_quantity"
            ],
            checks[
                "negative_inventory"
            ],
            checks[
                "invalid_sales_dates"
            ],
            checks[
                "sales_products_not_in_master"
            ]
        ]

        valid = all(
            value == 0
            for value in problems
        )

        return {
            "valid": valid,
            "status": (
                "VERIFIED"
                if valid
                else "REVIEW REQUIRED"
            ),
            "checks": checks
        }
