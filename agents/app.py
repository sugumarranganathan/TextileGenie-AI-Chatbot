import streamlit as st
import pandas as pd
import plotly.express as px

from workflow.graph import build_graph


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="TextileGenie AI Chatbot",
    page_icon="🧞",
    layout="wide"
)


# ==========================================================
# CUSTOM UI
# ==========================================================

st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="title">🧞 TextileGenie AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Autonomous AI Business Assistant for Textile Retail'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    return {

        "products":
            pd.read_csv(
                "data/products.csv"
            ),

        "sales":
            pd.read_csv(
                "data/sales.csv"
            ),

        "inventory":
            pd.read_csv(
                "data/inventory.csv"
            ),

        "purchase":
            pd.read_csv(
                "data/purchase.csv"
            )
    }


# ==========================================================
# LOAD LANGGRAPH
# ==========================================================

@st.cache_resource
def load_graph():

    return build_graph()


data = load_data()

graph = load_graph()


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("🧞 TextileGenie")

    st.write(
        "Ask your textile business questions "
        "in normal language."
    )

    st.divider()

    st.subheader("📊 Available Data")

    st.write(
        f"Products: {len(data['products']):,}"
    )

    st.write(
        f"Sales Records: {len(data['sales']):,}"
    )

    st.write(
        f"Inventory Records: {len(data['inventory']):,}"
    )

    st.write(
        f"Purchase Records: {len(data['purchase']):,}"
    )

    st.divider()

    st.subheader("💬 Example Questions")

    examples = [

        "Which products were not sold in the last 30 days?",

        "Which shirt brand moved fastest in the last 15 days?",

        "Which products are slow moving?",

        "Which products have low stock?",

        "What should I order this week?",

        "Which brands are growing?"
    ]

    for example in examples:

        st.write(
            f"• {example}"
        )


# ==========================================================
# WELCOME
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


if not st.session_state.messages:

    st.info(
        "👋 Welcome! Ask me anything about your "
        "textile shop's sales, inventory and purchases."
    )


# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ==========================================================
# CHAT INPUT
# ==========================================================

question = st.chat_input(
    "Ask TextileGenie about your business..."
)


# ==========================================================
# PROCESS QUESTION
# ==========================================================

if question:

    # --------------------------------------
    # USER MESSAGE
    # --------------------------------------

    st.session_state.messages.append({

        "role": "user",

        "content": question
    })

    with st.chat_message("user"):

        st.markdown(question)


    # --------------------------------------
    # ASSISTANT
    # --------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🧞 TextileGenie is analyzing..."
        ):

            initial_state = {

                "question":
                    question,

                "products_df":
                    data["products"],

                "sales_df":
                    data["sales"],

                "inventory_df":
                    data["inventory"],

                "purchase_df":
                    data["purchase"]
            }

            result = graph.invoke(
                initial_state
            )


        # ==================================
        # QUERY INFORMATION
        # ==================================

        intent = result.get(
            "intent",
            "sales_summary"
        )

        category = result.get(
            "category",
            ""
        )

        period = result.get(
            "period_days",
            30
        )


        st.caption(
            f"🧠 Intent: {intent} | "
            f"Period: {period} days"
        )


        # ==================================
        # RESULT
        # ==================================

        st.markdown(
            "## 🏆 Result"
        )


        # ==================================
        # UNSOLD PRODUCTS
        # ==================================

        if intent == "unsold_products":

            sales = data["sales"].copy()

            inventory = data[
                "inventory"
            ].copy()

            sales["Date"] = pd.to_datetime(
                sales["Date"]
            )

            latest_date = sales[
                "Date"
            ].max()

            start_date = (
                latest_date
                -
                pd.Timedelta(
                    days=period - 1
                )
            )

            recent = sales[
                sales["Date"] >= start_date
            ]

            if category:

                recent = recent[
                    recent["Category"]
                    .astype(str)
                    .str.lower()
                    .str.contains(
                        category.lower(),
                        na=False
                    )
                ]

                inventory = inventory[
                    inventory["Category"]
                    .astype(str)
                    .str.lower()
                    .str.contains(
                        category.lower(),
                        na=False
                    )
                ]

            sold_ids = set(
                recent[
                    "Product_ID"
                ]
            )

            unsold = inventory[
                ~inventory[
                    "Product_ID"
                ].isin(
                    sold_ids
                )
            ]

            st.error(
                f"🔴 {len(unsold)} products "
                f"had zero sales in the last "
                f"{period} days."
            )

            if not unsold.empty:

                st.dataframe(
                    unsold[
                        [
                            "Product_ID",
                            "Product_Name",
                            "Brand",
                            "Category",
                            "Size",
                            "Color",
                            "Current_Stock"
                        ]
                    ],
                    use_container_width=True
                )


        # ==================================
        # FAST MOVING
        # ==================================

        elif intent in [
            "fast_moving",
            "brand_sales"
        ]:

            analysis = result[
                "analysis"
            ]

            brand_sales = analysis[
                "brand_sales"
            ]

            if not brand_sales.empty:

                winner = (
                    brand_sales
                    .iloc[0]
                )

                st.success(
                    f"🥇 {winner['Brand']} "
                    f"is the fastest-moving "
                    f"brand with "
                    f"{int(winner['Quantity'])} "
                    f"units."
                )

                fig = px.bar(
                    brand_sales.head(10),

                    x="Brand",

                    y="Quantity",

                    title=(
                        f"Brand Movement — "
                        f"Last {period} Days"
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                st.dataframe(
                    brand_sales,
                    use_container_width=True
                )


        # ==================================
        # SLOW MOVING
        # ==================================

        elif intent == "slow_moving":

            inventory_result = result[
                "inventory_result"
            ]

            threshold = (
                inventory_result[
                    "Units_Sold"
                ].quantile(0.25)
            )

            slow = inventory_result[
                inventory_result[
                    "Units_Sold"
                ] <= threshold
            ]

            st.warning(
                f"🐌 {len(slow)} products "
                "are slow-moving."
            )

            st.dataframe(
                slow[
                    [
                        "Product_Name",
                        "Brand",
                        "Category",
                        "Current_Stock",
                        "Units_Sold"
                    ]
                ].head(30),

                use_container_width=True
            )


        # ==================================
        # LOW STOCK
        # ==================================

        elif intent == "low_stock":

            inventory_result = result[
                "inventory_result"
            ]

            low = inventory_result[
                inventory_result[
                    "Low_Stock"
                ]
            ]

            st.error(
                f"📦 {len(low)} products "
                "need stock review."
            )

            st.dataframe(
                low[
                    [
                        "Product_Name",
                        "Brand",
                        "Category",
                        "Current_Stock",
                        "Units_Sold",
                        "Days_of_Stock"
                    ]
                ].head(30),

                use_container_width=True
            )


        # ==================================
        # PURCHASE
        # ==================================

        elif intent == "purchase_recommendation":

            purchase = result[
                "purchase_result"
            ]

            st.warning(
                f"🛒 {len(purchase)} products "
                "should be reviewed for "
                "replenishment."
            )

            if not purchase.empty:

                st.dataframe(
                    purchase[
                        [
                            "Product_Name",
                            "Brand",
                            "Category",
                            "Current_Stock",
                            "Units_Sold",
                            "Days_of_Stock",
                            "Suggested_Order_Qty"
                        ]
                    ].head(30),

                    use_container_width=True
                )


        # ==================================
        # GENERAL SALES
        # ==================================

        else:

            analysis = result[
                "analysis"
            ]

            col1, col2 = st.columns(2)

            col1.metric(
                "Units Sold",
                f"{analysis['total_units']:,}"
            )

            col2.metric(
                "Revenue",
                f"₹{analysis['total_revenue']:,.0f}"
            )


        # ==================================
        # TREND
        # ==================================

        trend = result.get(
            "trend"
        )

        if (
            trend is not None
            and not trend.empty
        ):

            st.markdown(
                "## 📈 Brand Trends"
            )

            st.dataframe(
                trend,
                use_container_width=True
            )


        # ==================================
        # FORECAST
        # ==================================

        forecast = result.get(
            "forecast"
        )

        if forecast:

            st.markdown(
                "## 🔮 Demand Forecast"
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Average Daily Sales",
                forecast[
                    "daily_average"
                ]
            )

            col2.metric(
                "Expected Next 7 Days",
                forecast[
                    "next_7_days"
                ]
            )


        # ==================================
        # INSIGHTS
        # ==================================

        st.markdown(
            "## 💡 Business Insights"
        )

        for insight in result.get(
            "insights",
            []
        ):

            st.write(
                f"• {insight}"
            )


        # ==================================
        # RECOMMENDATIONS
        # ==================================

        st.markdown(
            "## 📝 Suggestions"
        )

        for recommendation in result.get(
            "recommendations",
            []
        ):

            st.write(
                f"• {recommendation}"
            )


        # ==================================
        # VALIDATION
        # ==================================

        st.markdown(
            "## 📊 Validation & Metrics"
        )

        validation = result[
            "validation"
        ]

        if validation["valid"]:

            st.success(
                "✅ Data validation passed."
            )

        else:

            st.warning(
                "⚠️ Data quality requires review."
            )

        with st.expander(
            "View validation details"
        ):

            st.json(
                validation["checks"]
            )


        # ==================================
        # SAVE ASSISTANT RESPONSE
        # ==================================

        summary = (
            "Analysis completed successfully. "
            f"Intent: {intent}. "
            f"Validation: "
            f"{validation['status']}."
        )

        st.session_state.messages.append({

            "role": "assistant",

            "content": summary
        })
