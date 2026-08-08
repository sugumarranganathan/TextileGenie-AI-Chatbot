# ==========================================================
# TEXTILEGENIE AI CHATBOT
# RULE-BASED AI
# PART 1
# ==========================================================

import re
import pandas as pd
import streamlit as st


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="TextileGenie AI Chatbot",
    page_icon="🧞",
    layout="wide"
)


# ==========================================================
# CUSTOM CSS
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
# SESSION STATE
# ==========================================================

if "input_mode" not in st.session_state:
    st.session_state.input_mode = "✍️ Custom Question"

if "custom_question" not in st.session_state:
    st.session_state.custom_question = ""

if "selected_example" not in st.session_state:
    st.session_state.selected_example = "Select a question"

if "question" not in st.session_state:
    st.session_state.question = None

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "analysis_question" not in st.session_state:
    st.session_state.analysis_question = None


# ==========================================================
# CLEAR CALLBACK
# IMPORTANT:
# Do NOT modify widget state after widget creation.
# The callback runs safely before the next Streamlit rerun.
# ==========================================================

def clear_question():

    st.session_state.custom_question = ""

    st.session_state.selected_example = "Select a question"

    st.session_state.question = None

    st.session_state.analysis_result = None

    st.session_state.analysis_question = None


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class="main-title">
        🧞 TextileGenie AI Chatbot
    </div>
    """,
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
# LOAD BUSINESS DATA
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


# ==========================================================
# LOAD DATA SAFELY
# ==========================================================

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
        ### Rule-Based AI Modules

        🧠 Query Understanding

        📊 Sales Analysis

        📦 Inventory Analysis

        🛒 Purchase Analysis

        💰 Price Analysis

        🏷️ Brand Analysis

        📈 Trend Analysis

        💡 Business Insights

        📝 Recommendations
        """
    )


# ==========================================================
# BUSINESS QUESTION UI
# ==========================================================

st.subheader(
    "💬 Ask Your Business Question"
)

st.write(
    "Ask TextileGenie about your textile business. "
    "Choose either a custom question or an example question."
)


# ==========================================================
# INPUT MODE
# ==========================================================

input_mode = st.radio(
    "Choose question type",
    [
        "✍️ Custom Question",
        "📋 Example Question"
    ],
    horizontal=True,
    key="input_mode"
)


# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

example_questions = [

    # ======================================================
    # SALES
    # ======================================================

    "Which products sold the most?",
    "Which products sold the most yesterday?",
    "Which products moved fastest?",
    "Which products moved fastest in the last 7 days?",
    "Which products moved fastest in the last 15 days?",
    "Which products moved fastest in the last 30 days?",
    "What are my top selling products?",
    "What are my best selling products?",
    "Which products have the highest sales?",
    "Which products have the lowest sales?",
    "Which products sold the least?",
    "Which category sold the most?",
    "Which category sold the least?",
    "Which brand sold the most?",
    "Which brand sold the least?",
    "What are my total sales?",
    "What were my sales yesterday?",
    "What were my sales last week?",
    "What were my sales last month?",
    "Show me my sales.",
    "Show me my sales for the last 7 days.",
    "Show me my sales for the last 15 days.",
    "Show me my sales for the last 30 days.",
    "How many products did I sell?",
    "How many units did I sell?",
    "What is my sales performance?",

    # ======================================================
    # INVENTORY
    # ======================================================

    "Which products were not sold?",
    "Which products have zero sales?",
    "Which products have no sales?",
    "Which products did not sell?",
    "Which products are unsold?",
    "Which products are running low in stock?",
    "Which products have low stock?",
    "Which products have the highest stock?",
    "Which products have the lowest stock?",
    "Which products have the most stock?",
    "Which products are overstocked?",
    "Which products are slow moving?",
    "Which products are slow selling?",
    "Which products are selling slowly?",
    "Which shirts are low in stock?",
    "Which jeans are low in stock?",
    "Which sarees are low in stock?",
    "Which pants are low in stock?",
    "Which kurtis are low in stock?",
    "Which dresses are low in stock?",
    "Which products are almost out of stock?",
    "Show me my current stock.",
    "Show me inventory.",
    "Which products need immediate restocking?",

    # ======================================================
    # PURCHASE
    # ======================================================

    "What products should I reorder?",
    "Which products should I purchase?",
    "Which products should I buy?",
    "Which products need urgent replenishment?",
    "Which products need restocking?",
    "What should I order this week?",
    "What should I purchase this month?",
    "Which brands should I purchase?",
    "Which products should I purchase more of?",
    "Which products should I stop purchasing?",
    "What should I reorder?",
    "What should I buy now?",
    "What should I purchase now?",
    "Which products need replenishment?",
    "Which products should I stock up on?",

    # ======================================================
    # PRICE
    # ======================================================

    "Which product is costly?",
    "Which shirt is costly?",
    "Which product is most expensive?",
    "Which shirts are most expensive?",
    "Which product is cheapest?",
    "Which shirt is cheapest?",
    "Which products have the highest price?",
    "Which products have the lowest price?",
    "Which product has the highest MRP?",
    "Which product has the lowest MRP?",
    "What is the selling price of the products?",
    "What is the purchase price of the products?",
    "Show me product prices.",
    "Show me selling prices.",
    "Show me purchase prices.",
    "Which product has the highest cost?",
    "Which product has the lowest cost?",
    "What is the price of this product?",
    "Which shirts are costly?",
    "Which jeans are costly?",
    "Which sarees are costly?",

    # ======================================================
    # BRAND
    # ======================================================

    "Which brand is performing best?",
    "Which brand is performing poorly?",
    "Which brand moved fastest?",
    "Which brand sells the most shirts?",
    "Which brand sells the most jeans?",
    "Which brand sells the most sarees?",
    "Which brand has the highest sales?",
    "Which brand has the lowest sales?",
    "Compare different brands.",
    "Show me brand sales.",
    "Show me brand performance.",

    # ======================================================
    # CATEGORY
    # ======================================================

    "Which category is performing best?",
    "Which category sells the most?",
    "Which category sells the least?",
    "Compare shirt and jeans sales.",
    "How are my saree sales?",
    "How are my shirt sales?",
    "How are my jeans sales?",
    "How are my pant sales?",
    "How are my kurti sales?",
    "How are my dress sales?",
    "Show me category sales.",
    "Compare my categories.",

    # ======================================================
    # TREND
    # ======================================================

    "Show me the sales trend.",
    "Which products are growing in sales?",
    "Which products are declining?",
    "Which products are improving?",
    "Which products are losing sales?",
    "Which brand has the best sales trend?",
    "Which category has the best trend?",
    "Are sales increasing or decreasing?",
    "Are my sales growing?",
    "Are my sales declining?",
    "Show me sales growth.",
    "Show me sales decline.",
    "What is the current sales trend?",

    # ======================================================
    # PROMOTION
    # ======================================================

    "Which products should I promote?",
    "Which products should I advertise?",
    "Which products need promotion?",
    "Which products should I promote this week?",
    "Which products should I promote today?",
    "Which slow products should I promote?",
    "What products should I advertise?",

    # ======================================================
    # DISCOUNT
    # ======================================================

    "Which products should I discount?",
    "Which products need a discount?",
    "Which products should I offer discounts on?",
    "Which products should I put on sale?",
    "Which slow products should I discount?",
    "What products should I discount this week?",

    # ======================================================
    # BUSINESS RECOMMENDATIONS
    # ======================================================

    "Which products should I keep more stock of?",
    "Which products should I reduce stock of?",
    "What should I focus on this week?",
    "Give me a business summary.",
    "Give me today's business summary.",
    "Give me a sales summary.",
    "Give me my business overview.",
    "What should I focus on?",
    "What products need attention?",
    "Which products require attention?",

    # ======================================================
    # BUDGET
    # ======================================================

    "What should I buy with a budget of 50000?",
    "What should I purchase with 50000?",
    "What should I buy with 100000?",
    "What should I purchase with 100000?",
    "Which products can I buy within 50000?",
    "Which products can I purchase within 50000?",
    "What should I buy within a budget of 50000?",
    "What should I buy within a budget of ₹50000?",
    "What should I purchase within ₹100000?"
]


# ==========================================================
# CUSTOM QUESTION MODE
# ==========================================================

if input_mode == "✍️ Custom Question":

    st.markdown(
        "✍️ **Type your own business question**"
    )

    custom_question = st.text_input(
        "Custom Question",
        placeholder=(
            "Example: Which shirt is costly in this shop?"
        ),
        label_visibility="collapsed",
        key="custom_question"
    )

    st.info(
        "✍️ You are using Custom Question mode."
    )


# ==========================================================
# EXAMPLE QUESTION MODE
# ==========================================================

else:

    st.markdown(
        "📋 **Select an example question**"
    )

    selected_example = st.selectbox(
        "Example Questions",
        [
            "Select a question"
        ] + example_questions,
        key="selected_example"
    )

    st.info(
        "📋 You are using Example Question mode."
    )


# ==========================================================
# BUTTONS
# ==========================================================

col1, col2 = st.columns(2)


# ==========================================================
# ANALYSE BUTTON
# ==========================================================

with col1:

    analyse_button = st.button(
        "🔍 Analyse",
        type="primary",
        use_container_width=True
    )


# ==========================================================
# CLEAR BUTTON
# ==========================================================

with col2:

    clear_button = st.button(
        "🧹 Clear",
        use_container_width=True,
        on_click=clear_question
    )


# ==========================================================
# SELECT QUESTION FOR ANALYSIS
# ==========================================================

if analyse_button:

    question = None

    # ------------------------------------------------------
    # CUSTOM QUESTION
    # ------------------------------------------------------

    if input_mode == "✍️ Custom Question":

        custom_text = st.session_state.custom_question.strip()

        if custom_text:

            question = custom_text

        else:

            st.warning(
                "⚠️ Please type your business question."
            )


    # ------------------------------------------------------
    # EXAMPLE QUESTION
    # ------------------------------------------------------

    elif input_mode == "📋 Example Question":

        selected_text = st.session_state.selected_example

        if (
            selected_text
            and
            selected_text != "Select a question"
        ):

            question = selected_text

        else:

            st.warning(
                "⚠️ Please select an example question."
            )


    # ------------------------------------------------------
    # SAVE QUESTION
    # ------------------------------------------------------

    if question:

        st.session_state.question = question

        st.session_state.analysis_question = question

        st.session_state.analysis_result = None


# ==========================================================
# ACTIVE QUESTION
# ==========================================================

question = st.session_state.question


# ==========================================================
# SHOW ACTIVE QUESTION
# ==========================================================

if question:

    st.markdown("---")

    st.markdown(
        "### 🔎 Question Being Analysed"
    )

    st.info(
        f"**{question}**"
    )


# ==========================================================
# QUERY UNDERSTANDING
# ==========================================================

def understand_question(question):

    q = question.lower().strip()


    # ======================================================
    # PERIOD
    # ======================================================

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

    elif "today" in q:

        period_days = 1

    elif "last week" in q:

        period_days = 7

    elif "last month" in q:

        period_days = 30

    elif "this week" in q:

        period_days = 7

    elif "this month" in q:

        period_days = 30


    # ======================================================
    # CATEGORY
    # ======================================================

    category = None

    categories = {

        "t-shirts": "T-Shirt",
        "t-shirt": "T-Shirt",

        "shirts": "Shirt",
        "shirt": "Shirt",

        "jeans": "Jeans",
        "jean": "Jeans",

        "pants": "Pant",
        "pant": "Pant",

        "kurtis": "Kurti",
        "kurti": "Kurti",

        "sarees": "Saree",
        "saree": "Saree",

        "dresses": "Dress",
        "dress": "Dress",

        "tops": "Top",
        "top": "Top",

        "jackets": "Jacket",
        "jacket": "Jacket"
    }

    # Longer keywords first
    # to avoid "shirt" matching inside "t-shirt"

    for keyword in sorted(
        categories.keys(),
        key=len,
        reverse=True
    ):

        if keyword in q:

            category = categories[keyword]

            break


    # ======================================================
    # INTENT
    # ======================================================

    intent = "sales_summary"


    # ------------------------------------------------------
    # UNSOLD
    # ------------------------------------------------------

    if (
        "not sold" in q
        or "unsold" in q
        or "zero sales" in q
        or "no sales" in q
        or "didn't sell" in q
        or "did not sell" in q
        or "no sale" in q
    ):

        intent = "unsold_products"


    # ------------------------------------------------------
    # FAST MOVING
    # ------------------------------------------------------

    elif (
        "fastest" in q
        or "fast moving" in q
        or "fast-moving" in q
        or "moved fast" in q
        or "best selling" in q
        or "best-selling" in q
        or "top selling" in q
        or "top-selling" in q
        or "most sold" in q
        or "selling fastest" in q
        or "sold the most" in q
        or "sell the most" in q
        or "highest sales" in q
    ):

        intent = "fast_moving"


    # ------------------------------------------------------
    # SLOW MOVING
    # ------------------------------------------------------

    elif (
        "slow moving" in q
        or "slow-moving" in q
        or "slow selling" in q
        or "slow-selling" in q
        or "poor selling" in q
        or "selling slowly" in q
        or "sold the least" in q
        or "lowest sales" in q
    ):

        intent = "slow_moving"


    # ------------------------------------------------------
    # LOW STOCK
    # ------------------------------------------------------

    elif (
        "low stock" in q
        or "running low" in q
        or "low inventory" in q
        or "stock is low" in q
        or "almost out of stock" in q
        or "urgent stock" in q
        or "out of stock" in q
        or "need restocking" in q
        or "need replenishment" in q
    ):

        intent = "low_stock"


    # ------------------------------------------------------
    # HIGH STOCK
    # ------------------------------------------------------

    elif (
        "highest stock" in q
        or "high stock" in q
        or "most stock" in q
        or "maximum stock" in q
        or "large stock" in q
        or "highest inventory" in q
    ):

        intent = "high_stock"


    # ------------------------------------------------------
    # OVERSTOCK
    # ------------------------------------------------------

    elif (
        "overstock" in q
        or "over stocked" in q
        or "too much stock" in q
        or "excess stock" in q
        or "excess inventory" in q
    ):

        intent = "overstocked"


    # ------------------------------------------------------
    # PURCHASE
    # ------------------------------------------------------

    elif (
        "reorder" in q
        or "purchase" in q
        or "buy" in q
        or "restock" in q
        or "replenish" in q
        or "what should i order" in q
        or "what should i purchase" in q
        or "what should i buy" in q
        or "what should i reorder" in q
        or "stock up" in q
    ):

        intent = "purchase_recommendation"


    # ------------------------------------------------------
    # PRICE
    # ------------------------------------------------------

    elif (
        "costly" in q
        or "costliest" in q
        or "expensive" in q
        or "most expensive" in q
        or "highest price" in q
        or "highest cost" in q
        or "maximum price" in q
        or "cheapest" in q
        or "lowest price" in q
        or "least expensive" in q
        or "lowest cost" in q
        or "minimum price" in q
        or "price of" in q
        or "cost of" in q
        or "selling price" in q
        or "purchase price" in q
        or "mrp" in q
        or "price" in q
        or "cost" in q
    ):

        intent = "price_analysis"


    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    elif (
        "brand" in q
        or "brands" in q
    ):

        intent = "brand_analysis"


    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    elif (
        "category" in q
        or "categories" in q
    ):

        intent = "category_analysis"


    # ------------------------------------------------------
    # TREND
    # ------------------------------------------------------

    elif (
        "trend" in q
        or "trending" in q
        or "growing" in q
        or "growth" in q
        or "declining" in q
        or "decline" in q
        or "increasing" in q
        or "decreasing" in q
        or "improving" in q
        or "losing sales" in q
    ):

        intent = "trend_analysis"


    # ------------------------------------------------------
    # PROMOTION
    # ------------------------------------------------------

    elif (
        "promote" in q
        or "promotion" in q
        or "advertise" in q
        or "advertising" in q
    ):

        intent = "promotion_recommendation"


    # ------------------------------------------------------
    # DISCOUNT
    # ------------------------------------------------------

    elif (
        "discount" in q
        or "discounts" in q
        or "offer" in q
        or "offers" in q
        or "sale offer" in q
    ):

        intent = "discount_recommendation"


    # ------------------------------------------------------
    # BUDGET
    # ------------------------------------------------------

    elif (
        "budget" in q
        or "₹" in q
        or "rs " in q
        or "rs." in q
        or "rupees" in q
    ):

        intent = "budget_recommendation"


    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------

    elif (
        "summary" in q
        or "overview" in q
        or "performance" in q
        or "business report" in q
        or "business overview" in q
    ):

        intent = "business_summary"


    # ======================================================
    # METRIC
    # ======================================================

    if (
        "revenue" in q
        or "sales value" in q
        or "sales amount" in q
        or "turnover" in q
    ):

        metric = "revenue"

    elif "profit" in q:

        metric = "profit"

    elif (
        "price" in q
        or "cost" in q
        or "mrp" in q
    ):

        metric = "price"

    else:

        metric = "units"


    # ======================================================
    # BUDGET EXTRACTION
    # ======================================================

    budget = None

    budget_patterns = [

        r"₹\s*([\d,]+)",

        r"rs\.?\s*([\d,]+)",

        r"rupees\s*([\d,]+)",

        r"budget\s*(?:of|is)?\s*₹?\s*([\d,]+)",

        r"([\d,]+)\s*rupees"

    ]

    for pattern in budget_patterns:

        match = re.search(
            pattern,
            q
        )

        if match:

            budget = float(
                match.group(1).replace(
                    ",",
                    ""
                )
            )

            break


    # ======================================================
    # RETURN QUERY UNDERSTANDING
    # ======================================================

    return {

        "question": question,

        "query": q,

        "intent": intent,

        "category": category,

        "period_days": period_days,

        "metric": metric,

        "budget": budget
    }


# ==========================================================
# DATA HELPER FUNCTIONS
# ==========================================================

def find_quantity_column(df):

    possible_columns = [

        "Quantity",

        "quantity",

        "Units",

        "Units_Sold",

        "Qty",

        "Sales_Quantity"

    ]

    for column in possible_columns:

        if column in df.columns:

            return column

    return None


# ==========================================================
# DATE COLUMN
# ==========================================================

def find_date_column(df):

    possible_columns = [

        "Date",

        "date",

        "Sale_Date",

        "Sales_Date",

        "Transaction_Date"

    ]

    for column in possible_columns:

        if column in df.columns:

            return column

    return None


# ==========================================================
# PRODUCT COLUMN
# ==========================================================

def find_product_column(df):

    possible_columns = [

        "Product_Name",

        "Product",

        "ProductName",

        "Product_Name "

    ]

    for column in possible_columns:

        if column in df.columns:

            return column

    return None


# ==========================================================
# PRICE COLUMN
# ==========================================================

def find_price_column(df):

    possible_columns = [

        "Selling_Price",

        "Selling Price",

        "MRP",

        "Purchase_Price",

        "Purchase Price",

        "Price",

        "price"

    ]

    for column in possible_columns:

        if column in df.columns:

            return column

    return None


# ==========================================================
# STOCK COLUMN
# ==========================================================

def find_stock_column(df):

    possible_columns = [

        "Current_Stock",

        "Current Stock",

        "Stock",

        "Quantity",

        "Available_Stock"

    ]

    for column in possible_columns:

        if column in df.columns:

            return column

    return None


# ==========================================================
# END OF PART 1
# ==========================================================

# ==========================================================
# TEXTILEGENIE AI CHATBOT
# PART 2
# ANALYSIS ENGINE + RESULTS + CHARTS
# ==========================================================


# ==========================================================
# PREPARE SALES DATA
# ==========================================================

def prepare_sales_data():

    df = sales_df.copy()

    date_column = find_date_column(df)

    if date_column:

        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )

    quantity_column = find_quantity_column(df)

    if quantity_column:

        df[quantity_column] = pd.to_numeric(
            df[quantity_column],
            errors="coerce"
        ).fillna(0)

    return df


# ==========================================================
# FILTER SALES DATA
# ==========================================================

def filter_sales_data(info):

    df = prepare_sales_data()

    date_column = find_date_column(df)

    if date_column:

        df = df.dropna(
            subset=[date_column]
        )

        if not df.empty:

            latest_date = df[
                date_column
            ].max()

            start_date = (
                latest_date
                - pd.Timedelta(
                    days=info["period_days"] - 1
                )
            )

            df = df[
                df[date_column] >= start_date
            ]

    # ------------------------------------------------------
    # CATEGORY FILTER
    # ------------------------------------------------------

    category = info["category"]

    if (
        category
        and "Category" in df.columns
    ):

        df = df[
            df["Category"]
            .astype(str)
            .str.lower()
            == category.lower()
        ]

    return df


# ==========================================================
# MERGE PRODUCT INFORMATION
# ==========================================================

def merge_product_information(df):

    if (
        "Product_ID" in df.columns
        and "Product_ID" in products_df.columns
    ):

        product_columns = [
            column
            for column in [
                "Product_ID",
                "Product_Name",
                "Category",
                "Brand",
                "Size",
                "Color",
                "MRP",
                "Purchase_Price",
                "Selling_Price"
            ]
            if column in products_df.columns
        ]

        product_data = products_df[
            product_columns
        ].drop_duplicates(
            subset=["Product_ID"]
        )

        df = df.merge(
            product_data,
            on="Product_ID",
            how="left",
            suffixes=("", "_product")
        )

    return df


# ==========================================================
# APPLY CATEGORY TO PRODUCTS
# ==========================================================

def filter_products_by_category(
    df,
    category
):

    if (
        category
        and "Category" in df.columns
    ):

        df = df[
            df["Category"]
            .astype(str)
            .str.lower()
            == category.lower()
        ]

    return df


# ==========================================================
# GET BRAND
# ==========================================================

def extract_brand(question):

    if "Brand" not in products_df.columns:

        return None

    brands = (
        products_df["Brand"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    question_lower = question.lower()

    for brand in brands:

        if brand.lower() in question_lower:

            return brand

    return None


# ==========================================================
# FILTER BY BRAND
# ==========================================================

def filter_by_brand(
    df,
    brand
):

    if (
        brand
        and "Brand" in df.columns
    ):

        df = df[
            df["Brand"]
            .astype(str)
            .str.lower()
            == brand.lower()
        ]

    return df


# ==========================================================
# SALES SUMMARY
# ==========================================================

def sales_summary(info):

    df = filter_sales_data(info)

    quantity_column = find_quantity_column(df)

    product_column = find_product_column(df)

    if quantity_column is None:

        return {
            "type": "error",
            "message":
                "Sales quantity column was not found."
        }

    if product_column is None:

        return {
            "type": "error",
            "message":
                "Product column was not found in sales data."
        }

    grouped = (
        df.groupby(
            product_column
        )[quantity_column]
        .sum()
        .reset_index()
        .sort_values(
            quantity_column,
            ascending=False
        )
    )

    grouped = grouped.head(10)

    return {

        "type": "table",

        "title":
            f"📊 Top Selling Products — "
            f"Last {info['period_days']} Days",

        "data": grouped,

        "message":
            "Here are the products with the highest "
            "sales quantity."
    }


# ==========================================================
# FAST MOVING PRODUCTS
# ==========================================================

def fast_moving_products(info):

    df = filter_sales_data(info)

    quantity_column = find_quantity_column(df)

    product_column = find_product_column(df)

    if (
        quantity_column is None
        or product_column is None
    ):

        return {
            "type": "error",
            "message":
                "Required sales columns were not found."
        }

    result = (
        df.groupby(
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

    return {

        "type": "table",

        "title":
            f"🔥 Fast-Moving Products — "
            f"Last {info['period_days']} Days",

        "data": result,

        "message":
            "These products have the strongest "
            "sales movement."
    }


# ==========================================================
# SLOW MOVING PRODUCTS
# ==========================================================

def slow_moving_products(info):

    df = filter_sales_data(info)

    quantity_column = find_quantity_column(df)

    product_column = find_product_column(df)

    if (
        quantity_column is None
        or product_column is None
    ):

        return {
            "type": "error",
            "message":
                "Required sales columns were not found."
        }

    result = (
        df.groupby(
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

    return {

        "type": "table",

        "title":
            f"🐢 Slow-Moving Products — "
            f"Last {info['period_days']} Days",

        "data": result,

        "message":
            "These products have the lowest "
            "sales movement."
    }


# ==========================================================
# UNSOLD PRODUCTS
# ==========================================================

def unsold_products(info):

    sales = filter_sales_data(info)

    if "Product_ID" not in sales.columns:

        return {
            "type": "error",
            "message":
                "Product_ID is required to identify "
                "unsold products."
        }

    if "Product_ID" not in products_df.columns:

        return {
            "type": "error",
            "message":
                "Product_ID is missing from products data."
        }

    sold_ids = set(
        sales[
            "Product_ID"
        ]
        .astype(str)
    )

    result = products_df[
        ~products_df[
            "Product_ID"
        ]
        .astype(str)
        .isin(sold_ids)
    ].copy()

    result = filter_products_by_category(
        result,
        info["category"]
    )

    return {

        "type": "table",

        "title":
            f"🚫 Products Not Sold — "
            f"Last {info['period_days']} Days",

        "data": result,

        "message":
            f"{len(result)} products had no sales "
            f"during the selected period."
    }


# ==========================================================
# INVENTORY HELPER
# ==========================================================

def inventory_with_products():

    df = inventory_df.copy()

    if (
        "Product_ID" in df.columns
        and "Product_ID" in products_df.columns
    ):

        product_columns = [
            column
            for column in [
                "Product_ID",
                "Product_Name",
                "Category",
                "Brand",
                "Size",
                "Color",
                "MRP",
                "Purchase_Price",
                "Selling_Price"
            ]
            if column in products_df.columns
        ]

        product_data = products_df[
            product_columns
        ].drop_duplicates(
            subset=["Product_ID"]
        )

        df = df.merge(
            product_data,
            on="Product_ID",
            how="left"
        )

    return df


# ==========================================================
# LOW STOCK
# ==========================================================

def low_stock_products(info):

    df = inventory_with_products()

    stock_column = find_stock_column(df)

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df[stock_column] = pd.to_numeric(
        df[stock_column],
        errors="coerce"
    ).fillna(0)

    result = df[
        df[stock_column] <= 10
    ].copy()

    result = filter_products_by_category(
        result,
        info["category"]
    )

    result = result.sort_values(
        stock_column,
        ascending=True
    )

    return {

        "type": "table",

        "title":
            "🔴 Low Stock Products",

        "data": result,

        "message":
            f"{len(result)} products are currently "
            f"running low in stock."
    }


# ==========================================================
# HIGH STOCK
# ==========================================================

def high_stock_products(info):

    df = inventory_with_products()

    stock_column = find_stock_column(df)

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df[stock_column] = pd.to_numeric(
        df[stock_column],
        errors="coerce"
    ).fillna(0)

    result = (
        df
        .sort_values(
            stock_column,
            ascending=False
        )
        .head(10)
    )

    result = filter_products_by_category(
        result,
        info["category"]
    )

    return {

        "type": "table",

        "title":
            "📦 Highest Stock Products",

        "data": result,

        "message":
            "These products currently have "
            "the highest inventory levels."
    }


# ==========================================================
# OVERSTOCKED PRODUCTS
# ==========================================================

def overstocked_products(info):

    df = inventory_with_products()

    stock_column = find_stock_column(df)

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df[stock_column] = pd.to_numeric(
        df[stock_column],
        errors="coerce"
    ).fillna(0)

    result = df[
        df[stock_column] >= 25
    ].copy()

    result = filter_products_by_category(
        result,
        info["category"]
    )

    result = result.sort_values(
        stock_column,
        ascending=False
    )

    return {

        "type": "table",

        "title":
            "📦 Overstocked Products",

        "data": result,

        "message":
            f"{len(result)} products have "
            "relatively high inventory levels."
    }


# ==========================================================
# PURCHASE RECOMMENDATION
# ==========================================================

def purchase_recommendation(info):

    inventory = inventory_with_products()

    stock_column = find_stock_column(
        inventory
    )

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    inventory[stock_column] = pd.to_numeric(
        inventory[stock_column],
        errors="coerce"
    ).fillna(0)

    result = inventory[
        inventory[stock_column] <= 10
    ].copy()

    result = filter_products_by_category(
        result,
        info["category"]
    )

    # Target stock
    TARGET_STOCK = 30

    result["Suggested_Order"] = (
        TARGET_STOCK
        - result[stock_column]
    ).clip(
        lower=0
    )

    # ------------------------------------------------------
    # ESTIMATED COST
    # ------------------------------------------------------

    purchase_price_column = None

    for column in [
        "Purchase_Price",
        "Purchase Price"
    ]:

        if column in result.columns:

            purchase_price_column = column

            break

    if purchase_price_column:

        result[purchase_price_column] = pd.to_numeric(
            result[purchase_price_column],
            errors="coerce"
        ).fillna(0)

        result["Estimated_Cost"] = (
            result["Suggested_Order"]
            * result[purchase_price_column]
        )

    result = result[
        result["Suggested_Order"] > 0
    ]

    result = result.sort_values(
        "Suggested_Order",
        ascending=False
    )

    return {

        "type": "table",

        "title":
            "🛒 Purchase Recommendation",

        "data": result,

        "message":
            "These low-stock products are candidates "
            "for replenishment."
    }


# ==========================================================
# PRICE ANALYSIS
# ==========================================================

def price_analysis(info):

    df = products_df.copy()

    df = filter_products_by_category(
        df,
        info["category"]
    )

    # ------------------------------------------------------
    # BRAND FILTER
    # ------------------------------------------------------

    detected_brand = info.get("brand")

    if detected_brand:

        df = filter_by_brand(
            df,
            detected_brand
        )

    price_column = find_price_column(
        df
    )

    if price_column is None:

        return {
            "type": "error",
            "message":
                "No price column was found in products data."
        }

    df[price_column] = pd.to_numeric(
        df[price_column],
        errors="coerce"
    )

    df = df.dropna(
        subset=[price_column]
    )

    q = info["query"]

    # ------------------------------------------------------
    # EXPENSIVE
    # ------------------------------------------------------

    if (
        "costly" in q
        or "costliest" in q
        or "expensive" in q
        or "most expensive" in q
        or "highest price" in q
        or "highest cost" in q
        or "maximum price" in q
    ):

        result = (
            df
            .sort_values(
                price_column,
                ascending=False
            )
            .head(10)
        )

        return {

            "type": "table",

            "title":
                "💰 Most Expensive Products",

            "data": result,

            "message":
                f"The highest-priced products are shown "
                f"using {price_column}."
        }

    # ------------------------------------------------------
    # CHEAPEST
    # ------------------------------------------------------

    if (
        "cheapest" in q
        or "lowest price" in q
        or "least expensive" in q
        or "lowest cost" in q
        or "minimum price" in q
    ):

        result = (
            df
            .sort_values(
                price_column,
                ascending=True
            )
            .head(10)
        )

        return {

            "type": "table",

            "title":
                "🏷️ Lowest-Priced Products",

            "data": result,

            "message":
                f"The lowest-priced products are shown "
                f"using {price_column}."
        }

    # ------------------------------------------------------
    # GENERAL PRICE
    # ------------------------------------------------------

    result = df.head(20)

    return {

        "type": "table",

        "title":
            "💰 Product Prices",

        "data": result,

        "message":
            "Here are the available product prices."
    }


# ==========================================================
# BRAND ANALYSIS
# ==========================================================

def brand_analysis(info):

    sales = filter_sales_data(info)

    sales = merge_product_information(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        quantity_column is None
        or "Brand" not in sales.columns
    ):

        return {
            "type": "error",
            "message":
                "Brand or sales quantity data was not found."
        }

    brand_sales = (
        sales
        .groupby("Brand")[quantity_column]
        .sum()
        .reset_index()
        .sort_values(
            quantity_column,
            ascending=False
        )
        .head(10)
    )

    return {

        "type": "table",

        "title":
            f"🏷️ Brand Sales Performance — "
            f"Last {info['period_days']} Days",

        "data": brand_sales,

        "message":
            "Brands are ranked according to sales quantity."
    }


# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

def category_analysis(info):

    sales = filter_sales_data(info)

    sales = merge_product_information(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        quantity_column is None
        or "Category" not in sales.columns
    ):

        return {
            "type": "error",
            "message":
                "Category or sales quantity data was not found."
        }

    category_sales = (
        sales
        .groupby("Category")[quantity_column]
        .sum()
        .reset_index()
        .sort_values(
            quantity_column,
            ascending=False
        )
    )

    return {

        "type": "table",

        "title":
            f"👕 Category Performance — "
            f"Last {info['period_days']} Days",

        "data": category_sales,

        "message":
            "Categories are ranked according to sales quantity."
    }


# ==========================================================
# TREND ANALYSIS
# ==========================================================

def trend_analysis(info):

    sales = filter_sales_data(info)

    date_column = find_date_column(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        date_column is None
        or quantity_column is None
    ):

        return {
            "type": "error",
            "message":
                "Date or quantity column was not found."
        }

    sales = sales.dropna(
        subset=[date_column]
    )

    # Apply category filter
    if (
        info["category"]
        and "Category" in sales.columns
    ):

        sales = sales[
            sales["Category"]
            .astype(str)
            .str.lower()
            ==
            info["category"].lower()
        ]

    trend = (
        sales
        .groupby(
            date_column
        )[quantity_column]
        .sum()
        .reset_index()
        .sort_values(
            date_column
        )
    )

    if len(trend) >= 2:

        first_value = float(
            trend[quantity_column].iloc[0]
        )

        last_value = float(
            trend[quantity_column].iloc[-1]
        )

        if last_value > first_value:

            direction = (
                "📈 Sales are increasing."
            )

        elif last_value < first_value:

            direction = (
                "📉 Sales are declining."
            )

        else:

            direction = (
                "➡️ Sales are relatively stable."
            )

    else:

        direction = (
            "Not enough data to calculate the trend."
        )

    return {

        "type": "chart",

        "title":
            "📈 Sales Trend",

        "data": trend,

        "date_column": date_column,

        "quantity_column": quantity_column,

        "message": direction
    }


# ==========================================================
# PROMOTION RECOMMENDATION
# ==========================================================

def promotion_recommendation(info):

    slow = slow_moving_products(
        info
    )

    if slow["type"] == "error":

        return slow

    return {

        "type": "table",

        "title":
            "📢 Products to Consider for Promotion",

        "data":
            slow["data"],

        "message":
            "Slow-moving products may benefit from "
            "promotions, bundles or targeted offers."
    }


# ==========================================================
# DISCOUNT RECOMMENDATION
# ==========================================================

def discount_recommendation(info):

    slow = slow_moving_products(
        info
    )

    if slow["type"] == "error":

        return slow

    return {

        "type": "table",

        "title":
            "🏷️ Products to Consider for Discount",

        "data":
            slow["data"],

        "message":
            "These slower-moving products may be "
            "candidates for a discount strategy."
    }


# ==========================================================
# BUDGET RECOMMENDATION
# ==========================================================

def budget_recommendation(info):

    budget = info["budget"]

    if budget is None:

        return {

            "type": "error",

            "message":
                "Please specify a budget. "
                "Example: What should I buy with ₹50,000?"
        }

    inventory = inventory_with_products()

    stock_column = find_stock_column(
        inventory
    )

    if stock_column is None:

        return {

            "type": "error",

            "message":
                "Stock information was not found."
        }

    purchase_price_column = None

    for column in [
        "Purchase_Price",
        "Purchase Price"
    ]:

        if column in inventory.columns:

            purchase_price_column = column

            break

    if purchase_price_column is None:

        return {

            "type": "error",

            "message":
                "Purchase price information was not found."
        }

    inventory[stock_column] = pd.to_numeric(
        inventory[stock_column],
        errors="coerce"
    ).fillna(0)

    inventory[purchase_price_column] = pd.to_numeric(
        inventory[purchase_price_column],
        errors="coerce"
    ).fillna(0)

    # ------------------------------------------------------
    # LOW STOCK PRODUCTS FIRST
    # ------------------------------------------------------

    inventory = inventory[
        inventory[stock_column] <= 10
    ].copy()

    inventory = filter_products_by_category(
        inventory,
        info["category"]
    )

    inventory["Suggested_Order"] = (
        30
        - inventory[stock_column]
    ).clip(
        lower=0
    )

    inventory["Estimated_Cost"] = (
        inventory["Suggested_Order"]
        *
        inventory[purchase_price_column]
    )

    inventory = inventory[
        inventory["Suggested_Order"] > 0
    ]

    # ------------------------------------------------------
    # SORT BY LOWER COST FIRST
    # ------------------------------------------------------

    inventory = inventory.sort_values(
        "Estimated_Cost",
        ascending=True
    )

    selected_rows = []

    remaining_budget = budget

    for _, row in inventory.iterrows():

        cost = float(
            row["Estimated_Cost"]
        )

        if cost <= remaining_budget:

            selected_rows.append(
                row
            )

            remaining_budget -= cost

    if selected_rows:

        result = pd.DataFrame(
            selected_rows
        )

    else:

        result = inventory.head(0)

    spent = (
        budget
        - remaining_budget
    )

    return {

        "type": "budget",

        "title":
            f"💰 Purchase Plan Within ₹{budget:,.0f}",

        "data": result,

        "budget": budget,

        "spent": spent,

        "remaining": remaining_budget,

        "message":
            f"Recommended products within your "
            f"₹{budget:,.0f} budget."
    }


# ==========================================================
# BUSINESS SUMMARY
# ==========================================================

def business_summary(info):

    sales = filter_sales_data(info)

    quantity_column = find_quantity_column(
        sales
    )

    inventory = inventory_with_products()

    stock_column = find_stock_column(
        inventory
    )

    if quantity_column is None:

        return {

            "type": "error",

            "message":
                "Sales quantity column was not found."
        }

    total_units = float(
        sales[quantity_column].sum()
    )

    low_stock_count = 0

    if stock_column:

        inventory[stock_column] = pd.to_numeric(
            inventory[stock_column],
            errors="coerce"
        ).fillna(0)

        low_stock_count = int(
            (
                inventory[stock_column] <= 10
            ).sum()
        )

    return {

        "type": "summary",

        "title":
            "📋 Business Summary",

        "total_units":
            total_units,

        "low_stock":
            low_stock_count,

        "sales_records":
            len(sales),

        "products":
            len(products_df),

        "message":
            f"During the selected period, "
            f"{total_units:,.0f} units were sold."
    }


# ==========================================================
# MAIN ANALYSIS ROUTER
# ==========================================================

def run_analysis(info):

    intent = info["intent"]

    # ------------------------------------------------------
    # SALES
    # ------------------------------------------------------

    if intent == "sales_summary":

        return sales_summary(info)

    if intent == "fast_moving":

        return fast_moving_products(info)

    if intent == "slow_moving":

        return slow_moving_products(info)


    # ------------------------------------------------------
    # INVENTORY
    # ------------------------------------------------------

    if intent == "unsold_products":

        return unsold_products(info)

    if intent == "low_stock":

        return low_stock_products(info)

    if intent == "high_stock":

        return high_stock_products(info)

    if intent == "overstocked":

        return overstocked_products(info)


    # ------------------------------------------------------
    # PURCHASE
    # ------------------------------------------------------

    if intent == "purchase_recommendation":

        return purchase_recommendation(info)


    # ------------------------------------------------------
    # PRICE
    # ------------------------------------------------------

    if intent == "price_analysis":

        return price_analysis(info)


    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    if intent == "brand_analysis":

        return brand_analysis(info)


    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    if intent == "category_analysis":

        return category_analysis(info)


    # ------------------------------------------------------
    # TREND
    # ------------------------------------------------------

    if intent == "trend_analysis":

        return trend_analysis(info)


    # ------------------------------------------------------
    # PROMOTION
    # ------------------------------------------------------

    if intent == "promotion_recommendation":

        return promotion_recommendation(info)


    # ------------------------------------------------------
    # DISCOUNT
    # ------------------------------------------------------

    if intent == "discount_recommendation":

        return discount_recommendation(info)


    # ------------------------------------------------------
    # BUDGET
    # ------------------------------------------------------

    if intent == "budget_recommendation":

        return budget_recommendation(info)


    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------

    if intent == "business_summary":

        return business_summary(info)


    # ------------------------------------------------------
    # DEFAULT
    # ------------------------------------------------------

    return sales_summary(info)


# ==========================================================
# DISPLAY TABLE
# ==========================================================

def display_table(data):

    if data is None:

        st.warning(
            "No data available."
        )

        return

    if data.empty:

        st.warning(
            "No matching records were found."
        )

        return

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# DISPLAY RESULT
# ==========================================================

def display_result(result):

    if result is None:

        return


    # ======================================================
    # ERROR
    # ======================================================

    if result["type"] == "error":

        st.error(
            result["message"]
        )

        return


    # ======================================================
    # TABLE
    # ======================================================

    if result["type"] == "table":

        st.success(
            result["message"]
        )

        st.markdown(
            f"### {result['title']}"
        )

        display_table(
            result["data"]
        )

        return


    # ======================================================
    # CHART
    # ======================================================

    if result["type"] == "chart":

        st.success(
            result["message"]
        )

        st.markdown(
            f"### {result['title']}"
        )

        chart_data = result["data"].copy()

        date_column = result[
            "date_column"
        ]

        quantity_column = result[
            "quantity_column"
        ]

        if not chart_data.empty:

            chart_data = chart_data.set_index(
                date_column
            )

            st.line_chart(
                chart_data[
                    quantity_column
                ]
            )

        return


    # ======================================================
    # BUDGET
    # ======================================================

    if result["type"] == "budget":

        st.success(
            result["message"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Budget",
                f"₹{result['budget']:,.0f}"
            )

        with col2:

            st.metric(
                "Estimated Spend",
                f"₹{result['spent']:,.0f}"
            )

        with col3:

            st.metric(
                "Remaining",
                f"₹{result['remaining']:,.0f}"
            )

        st.markdown(
            f"### {result['title']}"
        )

        display_table(
            result["data"]
        )

        return


    # ======================================================
    # SUMMARY
    # ======================================================

    if result["type"] == "summary":

        st.success(
            result["message"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Products",
                result["products"]
            )

        with col2:

            st.metric(
                "Sales Records",
                result["sales_records"]
            )

        with col3:

            st.metric(
                "Units Sold",
                f"{result['total_units']:,.0f}"
            )

        with col4:

            st.metric(
                "Low Stock Items",
                result["low_stock"]
            )

        st.markdown(
            "### 💡 Business Insight"
        )

        if result["low_stock"] > 0:

            st.warning(
                f"You currently have "
                f"{result['low_stock']} low-stock products. "
                f"Review replenishment before stock runs out."
            )

        else:

            st.info(
                "No products are currently below "
                "the low-stock threshold."
            )

        return


# ==========================================================
# BUSINESS RECOMMENDATION
# ==========================================================

def show_recommendation(
    info,
    result
):

    intent = info["intent"]

    st.markdown(
        "### 💡 Business Recommendation"
    )

    if intent == "fast_moving":

        st.info(
            "🔥 Prioritize these fast-moving products "
            "when planning your next purchase."
        )

    elif intent == "slow_moving":

        st.warning(
            "🐢 Consider promotions, bundles or "
            "smaller future purchases for slow-moving items."
        )

    elif intent == "unsold_products":

        st.warning(
            "📢 Consider discounts, bundles or "
            "promotional campaigns for products with no sales."
        )

    elif intent == "low_stock":

        st.warning(
            "📦 Review these products for replenishment, "
            "especially if they are also fast-moving."
        )

    elif intent == "high_stock":

        st.info(
            "📦 Monitor high-stock products carefully "
            "to avoid over-purchasing."
        )

    elif intent == "overstocked":

        st.warning(
            "📦 These products have relatively high stock. "
            "Consider slowing future purchases or using "
            "promotions to improve inventory movement."
        )

    elif intent == "purchase_recommendation":

        st.success(
            "🛒 Prioritize low-stock products and compare "
            "their recent sales movement before ordering."
        )

    elif intent == "price_analysis":

        st.info(
            "💰 Use price information together with sales "
            "movement before changing your product mix."
        )

    elif intent == "brand_analysis":

        st.success(
            "🏷️ Strong-performing brands can receive "
            "more purchasing and promotional attention."
        )

    elif intent == "category_analysis":

        st.success(
            "👕 Focus inventory and purchasing on categories "
            "with stronger demand."
        )

    elif intent == "trend_analysis":

        st.info(
            "📈 Use the trend direction to plan inventory "
            "and upcoming purchases."
        )

    elif intent == "promotion_recommendation":

        st.warning(
            "📢 Consider promoting slower-moving products "
            "to improve inventory turnover."
        )

    elif intent == "discount_recommendation":

        st.warning(
            "🏷️ Consider targeted discounts for products "
            "that remain slow-moving."
        )

    elif intent == "budget_recommendation":

        st.success(
            "💰 Prioritize products that need replenishment "
            "while keeping the purchase within your budget."
        )

    else:

        st.info(
            "📊 Review sales, inventory and purchase "
            "movement together before making a decision."
        )


# ==========================================================
# EXECUTE QUESTION
# ==========================================================

if (
    question
    and data_loaded
):

    st.markdown("---")

    st.subheader(
        "🤖 TextileGenie Analysis"
    )

    with st.spinner(
        "🧠 Analysing business data..."
    ):

        try:

            # ----------------------------------------------
            # UNDERSTAND QUESTION
            # ----------------------------------------------

            info = understand_question(
                question
            )


            # ----------------------------------------------
            # BRAND EXTRACTION
            # ----------------------------------------------

            detected_brand = extract_brand(
                question
            )

            info["brand"] = detected_brand


            # ----------------------------------------------
            # SHOW QUERY UNDERSTANDING
            # ----------------------------------------------

            with st.expander(
                "🔎 Query Understanding",
                expanded=True
            ):

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.write(
                        "**Intent**"
                    )

                    st.code(
                        info["intent"]
                    )

                with col2:

                    st.write(
                        "**Category**"
                    )

                    st.code(
                        str(
                            info["category"]
                        )
                    )

                with col3:

                    st.write(
                        "**Period**"
                    )

                    st.code(
                        f"{info['period_days']} days"
                    )

                with col4:

                    st.write(
                        "**Metric**"
                    )

                    st.code(
                        info["metric"]
                    )

                if info.get("brand"):

                    st.write(
                        f"**Brand:** "
                        f"{info['brand']}"
                    )

                if info.get("budget") is not None:

                    st.write(
                        "**Budget:** "
                        f"₹{info['budget']:,.0f}"
                    )


            # ----------------------------------------------
            # RUN ANALYSIS
            # ----------------------------------------------

            result = run_analysis(
                info
            )


            # ----------------------------------------------
            # STORE RESULT
            # ----------------------------------------------

            st.session_state.analysis_result = result


            # ----------------------------------------------
            # DISPLAY RESULT
            # ----------------------------------------------

            display_result(
                result
            )


            # ----------------------------------------------
            # BUSINESS RECOMMENDATION
            # ----------------------------------------------

            if result["type"] != "error":

                show_recommendation(
                    info,
                    result
                )


        except Exception as e:

            st.error(
                "❌ Analysis failed."
            )

            st.exception(e)


# ==========================================================
# NO QUESTION MESSAGE
# ==========================================================

elif (
    not question
    and data_loaded
):

    st.info(
        "👆 Choose Custom Question or Example Question, "
        "enter/select your question and click Analyse."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "🧞 TextileGenie AI — Rule-Based Textile Business Intelligence"
)
