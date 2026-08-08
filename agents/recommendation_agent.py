class RecommendationAgent:

    def __init__(self):
        self.name = "Recommendation Agent"

    def run(self, state):

        recommendations = []

        intent = state.get(
            "intent",
            ""
        )

        analysis = state.get(
            "analysis",
            {}
        )

        inventory = state.get(
            "inventory_result"
        )

        purchase = state.get(
            "purchase_result"
        )

        # -----------------------------
        # FAST MOVING
        # -----------------------------

        if intent == "fast_moving":

            recommendations.append(
                "🟢 Review stock of the fastest-moving products."
            )

            recommendations.append(
                "🟢 Check size and colour-level demand before ordering."
            )

            recommendations.append(
                "🟡 Compare recent movement with current inventory."
            )

        # -----------------------------
        # UNSOLD
        # -----------------------------

        elif intent == "unsold_products":

            recommendations.append(
                "🔴 Review products with zero sales before reordering."
            )

            recommendations.append(
                "🟡 Check size and colour movement."
            )

            recommendations.append(
                "💡 Consider merchandising or promotional actions where appropriate."
            )

        # -----------------------------
        # SLOW MOVING
        # -----------------------------

        elif intent == "slow_moving":

            recommendations.append(
                "🔴 Avoid increasing purchases of consistently slow-moving products."
            )

            recommendations.append(
                "💡 Review merchandising and promotional opportunities."
            )

        # -----------------------------
        # LOW STOCK
        # -----------------------------

        elif intent == "low_stock":

            recommendations.append(
                "🟠 Review low-stock products against recent sales velocity."
            )

            recommendations.append(
                "🟢 Prioritize products with strong recent movement."
            )

        # -----------------------------
        # PURCHASE
        # -----------------------------

        elif intent == "purchase_recommendation":

            recommendations.append(
                "🛒 Prioritize products with strong recent sales and limited stock."
            )

            recommendations.append(
                "📦 Check supplier availability before finalizing purchases."
            )

            recommendations.append(
                "🟡 Avoid over-ordering consistently slow-moving products."
            )

        # -----------------------------
        # TREND
        # -----------------------------

        elif intent == "trend":

            recommendations.append(
                "📈 Review brands showing sustained positive movement."
            )

            recommendations.append(
                "🔍 Investigate declining brands before increasing purchases."
            )

        else:

            recommendations.append(
                "📊 Review recent sales together with current inventory before making purchasing decisions."
            )

        # Universal recommendation
        recommendations.append(
            "✅ Use the latest verified sales and inventory data before making a purchase decision."
        )

        return recommendations
