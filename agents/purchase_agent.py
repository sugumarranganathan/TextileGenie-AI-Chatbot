class PurchaseAgent:

    def __init__(self):
        self.name = "Purchase Analysis Agent"

    def run(self, state):

        inventory_result = state[
            "inventory_result"
        ].copy()

        # Products needing replenishment
        reorder = inventory_result[
            (
                inventory_result["Low_Stock"]
            )
            &
            (
                inventory_result["Units_Sold"] > 0
            )
        ].copy()

        # Priority score
        reorder["Priority_Score"] = (
            reorder["Units_Sold"]
            /
            (
                reorder["Current_Stock"] + 1
            )
        )

        reorder = reorder.sort_values(
            "Priority_Score",
            ascending=False
        )

        # Suggested quantity
        reorder["Suggested_Order_Qty"] = (
            reorder["Units_Sold"]
            * 2
            -
            reorder["Current_Stock"]
        )

        reorder["Suggested_Order_Qty"] = (
            reorder["Suggested_Order_Qty"]
            .clip(lower=0)
            .round()
            .astype(int)
        )

        return reorder
