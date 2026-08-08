# ==========================================================
# TEXTILEGENIE AI CHATBOT
# RULE-BASED AI STREAMLIT APPLICATION
# ==========================================================

import re
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

    .question-box {
        padding: 15px;
        border-radius: 12px;
        background-color: #f7f9fc;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    .or-text {
        text-align: center;
        font-weight: 700;
        color: #777777;
        margin: 12px 0;
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
    AI-Powered Textile Retail Business Assistant
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
        **Rule-Based AI Modules**

        🧠 Query Understanding  
        👑 Business Routing  
        📊 Sales Analysis  
        📦 Inventory Analysis  
        🛒 Purchase Analysis  
        📈 Trend Analysis  
        💡 Business Insights  
        📝 Recommendations
        """
    )


# ==========================================================
# BUSINESS QUESTION SECTION
# ==========================================================

st.subheader(
    "💬 Ask Your Business Question"
)

st.markdown(
    """
    Ask TextileGenie about your textile business.
    You can type your own question or select an example.
    """
)


# ==========================================================
# CUSTOM QUESTION
# ==========================================================

custom_question = st.text_input(
    "✍️ Type your own business question",
    placeholder="Example: Which shirts sold the most in the last 10 days?"
)


# ==========================================================
# OR
# ==========================================================

st.markdown(
    '<div class="or-text">OR</div>',
    unsafe_allow_html=True
)


# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

example_questions = [

    "Which products moved fastest in the last 15 days?",

    "Which products were not sold?",

    "Which products are running low in stock?",

    "Which brand moved fastest?",

    "What products should I reorder?",

    "Show me the sales trend.",

    "Which shirts sold the most?",

    "Which jeans are selling fastest?",

    "Which products have zero sales?",

    "Which products need urgent restocking?",

    "Which products have the highest stock?",

    "Which products are slow-moving?",

    "What should I purchase this week?",

    "Which products should I promote?",

    "Which products are performing best?"
]


selected_example = st.selectbox(
    "📋 Example Questions",
    ["Select a question"] + example_questions
)


# ==========================================================
# ANALYSE BUTTON
# ==========================================================

analyse_button = st.button(
    "🔍 Analyse",
    type="primary",
    use_container_width=True
)


# ==========================================================
# QUESTION SELECTION
# ==========================================================

question = None

if analyse_button:

    if custom_question.strip():

        question = custom_question.strip()

    elif selected_example != "Select a question":

        question = selected_example

    else:

        st.warning(
            "Please type a question or select an example question."
        )


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


# ==========================================================
# FIND QUANTITY COLUMN
# ==========================================================

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


# ==========================================================
# FIND DATE COLUMN
# ==========================================================

def find_date_column(df):

    possible = [

        "Date",

        "date",

        "Sale_Date",

        "Sales_Date"
    ]

    for column in possible:

        if column in df.columns:

            return column

    return None


# ==========================================================
# FIND PRODUCT COLUMN
# ==========================================================

def find_product_column(df):

    possible = [

        "Product_Name",

        "Product",

        "ProductName"
    ]

    for column in possible:

        if column in df.columns:

            return column

    return None


# ==========================================================
# GET PERIOD
# ==========================================================

def get_period_days(q):

    period_days = 30

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

    elif "last month" in q:

        period_days = 30

    elif "this week" in q:

        period_days = 7

    elif "this month" in q:

        period_days = 30

    return period_days


# ==========================================================
# GET CATEGORY
# ==========================================================

def get_category(q):

    categories = {

        "shirt": "Shirt",

        "shirts": "Shirt",

        "t-shirt": "T-Shirt",

        "t-shirts": "T-Shirt",

        "jean": "Jeans",

        "jeans": "Jeans",

        "pant": "Pant",

        "pants": "Pant",

        "kurti": "Kurti",

        "kurtis": "Kurti",

        "saree": "Saree",

        "sarees": "Saree",

        "dress": "Dress",

        "dresses": "Dress"
    }

    for keyword, category in categories.items():

        if keyword in q:

            return category

    return None


# ==========================================================
# BUSINESS ANALYSIS
# ==========================================================

def analyse_question(question):

    q = question.lower().strip()

    sales = prepare_sales_data(
        sales_df
    )

    result = {}

    # ------------------------------------------------------
    # PERIOD
    # ------------------------------------------------------

    period_days = get_period_days(
        q
    )

    # ------------------------------------------------------
    # QUANTITY
    # ------------------------------------------------------

    quantity_column = find_quantity_column(
        sales
    )

    if quantity_column is None:

        return {
            "type": "error",
            "message":
                "Sales quantity column was not found."
        }

    # ------------------------------------------------------
    # DATE
    # ------------------------------------------------------

    date_column = find_date_column(
        sales
    )

    if date_column:

        sales = sales.dropna(
            subset=[date_column]
        )

        if not sales.empty:

            latest_date = sales[
                date_column
            ].max()

            start_date = (
                latest_date
                - pd.Timedelta(
                    days=period_days - 1
                )
            )

            filtered_sales = sales[
                sales[date_column]
                >= start_date
            ]

        else:

            filtered_sales = sales

    else:

        filtered_sales = sales

    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    category = get_category(
        q
    )

    if (
        category
        and "Category" in filtered_sales.columns
    ):

        filtered_sales = filtered_sales[
            filtered_sales[
                "Category"
            ]
            .astype(str)
            .str.lower()
            == category.lower()
        ]

    # ------------------------------------------------------
    # PRODUCT COLUMN
    # ------------------------------------------------------

    product_column = find_product_column(
        filtered_sales
    )

    # ======================================================
    # FAST MOVING PRODUCTS
    # ======================================================

    if (
        "fast" in q
        or "best selling" in q
        or "best-selling" in q
        or "top selling" in q
        or "top-selling" in q
        or "moved fast" in q
        or "most sold" in q
        or "selling most" in q
        or "selling fastest" in q
    ):

        if product_column:

            result_df = (

                filtered_sales

                .groupby(
                    product_column
                )[quantity_column]

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

    # ======================================================
    # UNSOLD PRODUCTS
    # ======================================================

    if (
        "not sold" in q
        or "unsold" in q
        or "zero sales" in q
        or "no sales" in q
        or "didn't sell" in q
        or "did not sell" in q
    ):

        if (
            "Product_ID" in products_df.columns
            and "Product_ID" in filtered_sales.columns
        ):

            sold_ids = set(
                filtered_sales[
                    "Product_ID"
                ]
                .astype(str)
            )

            unsold = products_df[
                ~products_df[
                    "Product_ID"
                ]
                .astype(str)
                .isin(sold_ids)
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

    # ======================================================
    # LOW STOCK
    # ======================================================

    if (
        "low stock" in q
        or "running low" in q
        or "low inventory" in q
        or "stock is low" in q
        or "almost out of stock" in q
        or "urgent stock" in q
        or "urgent replenishment" in q
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

            low_stock = (

                inventory_df[
                    inventory_df[
                        stock_column
                    ] <= 10
                ]

                .sort_values(
                    stock_column
                )
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

    # ======================================================
    # HIGH STOCK
    # ======================================================

    if (
        "highest stock" in q
        or "high stock" in q
        or "most stock" in q
        or "maximum stock" in q
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

            high_stock = (

                inventory_df

                .sort_values(
                    stock_column,
                    ascending=False
                )

                .head(10)
            )

            result["type"] = "table"

            result["title"] = (
                "📦 Highest Stock Products"
            )

            result["data"] = high_stock

            result["message"] = (
                "These products currently have "
                "the highest inventory levels."
            )

            return result

    # ======================================================
    # PURCHASE / REORDER
    # ======================================================

    if (
        "reorder" in q
        or "purchase" in q
        or "buy" in q
        or "restock" in q
        or "order" in q
        or "replenish" in q
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

                30
                - reorder[stock_column]

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

    # ======================================================
    # SLOW MOVING
    # ======================================================

    if (
        "slow moving" in q
        or "slow-moving" in q
        or "slow selling" in q
        or "poor selling" in q
    ):

        if product_column:

            slow = (

                filtered_sales

                .groupby(
                    product_column
                )[quantity_column]

                .sum()

                .reset_index()

                .sort_values(
                    quantity_column,
                    ascending=True
                )

                .head(10)
            )

            result["type"] = "table"

            result["title"] = (
                f"🐢 Slow-Moving Products "
                f"— Last {period_days} Days"
            )

            result["data"] = slow

            result["message"] = (
                "These products have the lowest "
                "sales quantity during the selected period."
            )

            return result

    # ======================================================
    # DEFAULT SALES SUMMARY
    # ======================================================

    if product_column:

        summary = (

            filtered_sales

            .groupby(
                product_column
            )[quantity_column]

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

    # ======================================================
    # UNKNOWN QUESTION
    # ======================================================

    return {

        "type": "error",

        "message":
            "I could not understand this business question. "
            "Try asking about sales, products, inventory, "
            "stock, purchases, reorder, or trends."
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

            # ==================================================
            # TABLE RESULT
            # ==================================================

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

                # ==============================================
                # VISUAL ANALYSIS
                # ==============================================

                chart_df = result["data"]

                if len(chart_df) > 0:

                    numeric_columns = (

                        chart_df

                        .select_dtypes(
                            include="number"
                        )

                        .columns

                        .tolist()
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

                # ==============================================
                # BUSINESS SUGGESTIONS
                # ==============================================

                st.markdown(
                    "### 💡 Business Suggestions"
                )

                q_lower = question.lower()

                if (
                    "low stock" in q_lower
                    or "reorder" in q_lower
                    or "purchase" in q_lower
                    or "restock" in q_lower
                    or "replenish" in q_lower
                    or "buy" in q_lower
                ):

                    st.info(
                        "🛒 Review these products and "
                        "consider replenishing fast-moving "
                        "items first."
                    )

                elif (
                    "not sold" in q_lower
                    or "unsold" in q_lower
                    or "zero sales" in q_lower
                ):

                    st.warning(
                        "📢 Consider discounts, bundles, "
                        "promotions, or moving these products "
                        "to a better-selling category."
                    )

                elif (
                    "slow" in q_lower
                ):

                    st.warning(
                        "🐢 Consider promotional offers, "
                        "bundles, or reducing future purchases "
                        "for slow-moving products."
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
    "🧞 TextileGenie AI • AI-Powered Textile Retail Business Assistant"
)
