# ==========================================================
# TEXTILEGENIE AI CHATBOT
# STREAMLIT APPLICATION
# ==========================================================

import os
import pandas as pd
import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
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

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 25px;
    }

    .result-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #f7f9fc;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    .success-text {
        color: #16803c;
        font-weight: 700;
    }

    .warning-text {
        color: #b45309;
        font-weight: 700;
    }

    .danger-text {
        color: #dc2626;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🧞 TextileGenie AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Autonomous AI Business Assistant for Textile Retail Shops
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    products = pd.read_csv(
        "data/products.csv"
    )

    sales = pd.read_csv(
        "data/sales.csv"
    )

    inventory = pd.read_csv(
        "data/inventory.csv"
    )

    purchase = pd.read_csv(
        "data/purchase.csv"
    )

    return (
        products,
        sales,
        inventory,
        purchase
    )


try:

    (
        products_df,
        sales_df,
        inventory_df,
        purchase_df
    ) = load_data()

    data_loaded = True

except Exception as e:

    data_loaded = False

    st.error(
        f"Unable to load business data: {e}"
    )


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("🧞 TextileGenie")

    st.markdown(
        "### Business Data"
    )

    if data_loaded:

        st.success(
            "Business data loaded"
        )

        st.metric(
            "Products",
            len(products_df)
        )

        st.metric(
            "Sales Records",
            len(sales_df)
        )

        st.metric(
            "Inventory Records",
            len(inventory_df)
        )

        st.metric(
            "Purchase Records",
            len(purchase_df)
        )

    st.markdown("---")

    st.markdown(
        """
        **Agents**

        🧠 Query Understanding  
        👑 Supervisor  
        📊 Sales  
        📦 Inventory  
        🛒 Purchase  
        📈 Trend  
        🔮 Forecast  
        💡 Insight  
        📝 Recommendation  
        ✅ Validation
        """
    )


# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

st.subheader("💬 Ask Your Business Question")

st.markdown(
    """
    Ask TextileGenie questions about your textile shop.
    """
)

example_questions = [
    "Which products moved fastest in the last 15 days?",
    "Which products were not sold?",
    "Which products are running low in stock?",
    "Which brand moved fastest?",
    "What products should I reorder?",
    "Show me the sales trend."
]


selected_example = st.selectbox(
    "Example questions",
    ["Select a question"] + example_questions
)


question = st.chat_input(
    "Ask something about your textile business..."
)


if question is None and selected_example != "Select a question":

    question = selected_example


# ==========================================================
# BUSINESS ANALYSIS FUNCTIONS
# ==========================================================

def prepare_sales_data(df):

    df = df.copy()

    date_columns = [
        "Date",
        "date",
        "Sale_Date",
        "Sales_Date"
    ]

    for column in date_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            break

    return df


def find_quantity_column(df):

    possible = [
        "Quantity",
        "quantity",
        "Units",
        "Units_Sold",
        "Number_of_Vehicles"
    ]

    for column in possible:

        if column in df.columns:

            return column

    return None


def analyse_question(question):

    q = question.lower()

    sales = prepare_sales_data(
        sales_df
    )

    result = {}

    # ------------------------------------------------------
    # PERIOD
    # ------------------------------------------------------

    period_days = 30

    import re

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

    elif "last week" in q:

        period_days = 7

    # ------------------------------------------------------
    # QUANTITY COLUMN
    # ------------------------------------------------------

    quantity_column = find_quantity_column(
        sales
    )

    if quantity_column is None:

        return {
            "type": "error",
            "message": "Sales quantity column was not found."
        }

    # ------------------------------------------------------
    # DATE FILTER
    # ------------------------------------------------------

    date_column = None

    for column in [
        "Date",
        "date",
        "Sale_Date",
        "Sales_Date"
    ]:

        if column in sales.columns:

            date_column = column
            break

    if date_column:

        sales = sales.dropna(
            subset=[date_column]
        )

        if not sales.empty:

            latest_date = sales[
                date_column
            ].max()

            start_date = (
                latest_date -
                pd.Timedelta(
                    days=period_days - 1
                )
            )

            filtered_sales = sales[
                sales[date_column] >= start_date
            ]

        else:

            filtered_sales = sales

    else:

        filtered_sales = sales

    # ------------------------------------------------------
    # CATEGORY FILTER
    # ------------------------------------------------------

    category = None

    categories = [
        "shirt",
        "t-shirt",
        "jeans",
        "pant",
        "kurti",
        "saree",
        "dress"
    ]

    for item in categories:

        if item in q:

            category = item

            if category == "shirt":

                category = "Shirt"

            elif category == "t-shirt":

                category = "T-Shirt"

            elif category == "jeans":

                category = "Jeans"

            elif category == "pant":

                category = "Pant"

            elif category == "kurti":

                category = "Kurti"

            elif category == "saree":

                category = "Saree"

            break

    if (
        category
        and "Category" in filtered_sales.columns
    ):

        filtered_sales = filtered_sales[
            filtered_sales["Category"]
            .astype(str)
            .str.lower()
            == category.lower()
        ]

    # ------------------------------------------------------
    # PRODUCT NAME COLUMN
    # ------------------------------------------------------

    product_column = None

    for column in [
        "Product_Name",
        "Product",
        "ProductName"
    ]:

        if column in filtered_sales.columns:

            product_column = column
            break

    # ------------------------------------------------------
    # FAST MOVING
    # ------------------------------------------------------

    if (
        "fast" in q
        or "best selling" in q
        or "top selling" in q
        or "moved fast" in q
    ):

        if product_column:

            result_df = (
                filtered_sales
                .groupby(product_column)[
                    quantity_column
                ]
                .sum()
                .reset_index()
                .sort_values(
                    quantity_column,
                    ascending=False
                )
                .head(10)
            )

            result["type"] = "table"

            result["title"] = (
                f"🔥 Fast-Moving Products "
                f"— Last {period_days} Days"
            )

            result["data"] = result_df

            result["message"] = (
                "These products have the highest "
                "sales quantity during the selected period."
            )

            return result

    # ------------------------------------------------------
    # UNSOLD PRODUCTS
    # ------------------------------------------------------

    if (
        "not sold" in q
        or "unsold" in q
        or "zero sales" in q
        or "no sales" in q
    ):

        if (
            "Product_ID" in products_df.columns
            and "Product_ID" in filtered_sales.columns
        ):

            sold_ids = set(
                filtered_sales[
                    "Product_ID"
                ].astype(str)
            )

            unsold = products_df[
                ~products_df[
                    "Product_ID"
                ].astype(str).isin(
                    sold_ids
                )
            ].copy()

            result["type"] = "table"

            result["title"] = (
                f"🚫 Products Not Sold "
                f"— Last {period_days} Days"
            )

            result["data"] = unsold

            result["message"] = (
                f"{len(unsold)} products "
                "had no sales in the selected period."
            )

            return result

    # ------------------------------------------------------
    # LOW STOCK
    # ------------------------------------------------------

    if (
        "low stock" in q
        or "running low" in q
        or "low inventory" in q
    ):

        stock_column = None

        for column in [
            "Current_Stock",
            "Stock",
            "Quantity"
        ]:

            if column in inventory_df.columns:

                stock_column = column
                break

        if stock_column:

            low_stock = inventory_df[
                inventory_df[
                    stock_column
                ] <= 10
            ].sort_values(
                stock_column
            )

            result["type"] = "table"

            result["title"] = (
                "🔴 Low Stock Products"
            )

            result["data"] = low_stock

            result["message"] = (
                f"{len(low_stock)} products "
                "are currently running low."
            )

            return result

    # ------------------------------------------------------
    # PURCHASE / REORDER
    # ------------------------------------------------------

    if (
        "reorder" in q
        or "purchase" in q
        or "buy" in q
        or "restock" in q
        or "order" in q
    ):

        stock_column = None

        for column in [
            "Current_Stock",
            "Stock",
            "Quantity"
        ]:

            if column in inventory_df.columns:

                stock_column = column
                break

        if stock_column:

            reorder = inventory_df[
                inventory_df[
                    stock_column
                ] <= 10
            ].copy()

            reorder[
                "Suggested_Order"
            ] = (
                30 -
                reorder[stock_column]
            ).clip(
                lower=0
            )

            result["type"] = "table"

            result["title"] = (
                "🛒 Purchase Recommendation"
            )

            result["data"] = reorder

            result["message"] = (
                "Products with low stock are "
                "recommended for replenishment."
            )

            return result

    # ------------------------------------------------------
    # DEFAULT SALES SUMMARY
    # ------------------------------------------------------

    if product_column:

        summary = (
            filtered_sales
            .groupby(product_column)[
                quantity_column
            ]
            .sum()
            .reset_index()
            .sort_values(
                quantity_column,
                ascending=False
            )
            .head(10)
        )

        result["type"] = "table"

        result["title"] = (
            "📊 Sales Summary"
        )

        result["data"] = summary

        result["message"] = (
            "Here is the current sales summary."
        )

        return result

    return {
        "type": "error",
        "message": "I could not understand this business question."
    }


# ==========================================================
# DISPLAY ANSWER
# ==========================================================

if question and data_loaded:

    st.markdown("---")

    st.subheader(
        "🤖 TextileGenie Analysis"
    )

    with st.spinner(
        "🧠 Analysing your business data..."
    ):

        try:

            result = analyse_question(
                question
            )

            if result["type"] == "table":

                st.success(
                    result["message"]
                )

                st.markdown(
                    f"### {result['title']}"
                )

                st.dataframe(
                    result["data"],
                    use_container_width=True,
                    hide_index=True
                )

                # --------------------------------------------------
                # SIMPLE CHART
                # --------------------------------------------------

                chart_df = result["data"]

                if len(chart_df) > 0:

                    numeric_columns = (
                        chart_df.select_dtypes(
                            include="number"
                        ).columns.tolist()
                    )

                    if numeric_columns:

                        st.markdown(
                            "### 📈 Visual Analysis"
                        )

                        st.bar_chart(
                            chart_df.set_index(
                                chart_df.columns[0]
                            )[numeric_columns[0]]
                        )

                # --------------------------------------------------
                # BUSINESS SUGGESTIONS
                # --------------------------------------------------

                st.markdown(
                    "### 💡 Business Suggestions"
                )

                if (
                    "low stock" in question.lower()
                    or "reorder" in question.lower()
                    or "purchase" in question.lower()
                ):

                    st.info(
                        "🛒 Review these products and "
                        "consider replenishing the fast-moving items first."
                    )

                elif (
                    "not sold" in question.lower()
                    or "unsold" in question.lower()
                ):

                    st.warning(
                        "📢 Consider discounts, bundles, "
                        "promotions, or moving these products "
                        "to a better-selling category."
                    )

                else:

                    st.info(
                        "📈 Focus inventory and purchasing "
                        "on products showing stronger sales movement."
                    )

            else:

                st.error(
                    result["message"]
                )

        except Exception as e:

            st.error(
                "Analysis error"
            )

            st.exception(e)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "🧞 TextileGenie AI • Autonomous Textile Retail Business Assistant"
)
