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
