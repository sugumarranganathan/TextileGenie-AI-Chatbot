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

        🧠 Natural Language Query Understanding

        📊 Sales Analysis

        📦 Inventory Analysis

        🛒 Purchase Analysis

        💰 Price Analysis

        🏷️ Brand Analysis

        👕 Category Analysis

        📈 Trend Analysis

        📢 Promotion Recommendation

        🏷️ Discount Recommendation

        💰 Budget Recommendation

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
    "You can type your own question naturally or select an example."
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
# COMPREHENSIVE EXAMPLE QUESTIONS
# ==========================================================

example_questions = [

    # ======================================================
    # SALES
    # ======================================================

    "Which products sold the most?",
    "What products are selling the most?",
    "Which products are best sellers?",
    "What are my top selling products?",
    "Which products have the highest sales?",
    "Which products moved fastest?",
    "Which products moved fastest in the last 7 days?",
    "Which products moved fastest in the last 15 days?",
    "Which products moved fastest in the last 30 days?",
    "What sold well recently?",
    "What are customers buying the most?",
    "Which items are selling well?",
    "Which products have good sales?",
    "What products have strong demand?",
    "Which products sold the least?",
    "Which products have the lowest sales?",
    "What are my worst selling products?",
    "How many units did I sell?",
    "How many products did I sell?",
    "What were my sales yesterday?",
    "What were my sales last week?",
    "What were my sales last month?",
    "What are my total sales?",
    "Show me my sales.",
    "Show me today's sales.",
    "Show me last week's sales.",
    "Show me last month's sales.",
    "Give me my sales performance.",
    "How is my business selling?",
    "How are my sales doing?",

    # ======================================================
    # FAST MOVING
    # ======================================================

    "Which products are fast moving?",
    "Which products are moving quickly?",
    "Which items are moving fast?",
    "Which products sell quickly?",
    "What products are selling quickly?",
    "Which products have the highest demand?",
    "Which products are my best movers?",
    "What is moving fastest?",
    "Which shirts are selling fastest?",
    "Which jeans are selling fastest?",
    "Which sarees are selling fastest?",

    # ======================================================
    # SLOW MOVING
    # ======================================================

    "Which products are slow moving?",
    "Which products are slow selling?",
    "Which items are moving slowly?",
    "Which products are selling slowly?",
    "Which products are poor sellers?",
    "Which products are weak sellers?",
    "Which products have poor sales?",
    "Which products sold the least?",
    "Which products are not moving well?",
    "What products are stuck in inventory?",
    "Which shirts are slow selling?",
    "Which jeans are slow selling?",
    "Which sarees are slow selling?",

    # ======================================================
    # UNSOLD
    # ======================================================

    "Which products were not sold?",
    "Which products have no sales?",
    "Which products have zero sales?",
    "Which products did not sell?",
    "Which products didn't sell?",
    "Which products are unsold?",
    "What products have no sales?",
    "Show me unsold products.",
    "Are there products that nobody bought?",
    "Which products have not moved?",

    # ======================================================
    # LOW STOCK
    # ======================================================

    "Which products are running low in stock?",
    "Which products have low stock?",
    "Which products are low on stock?",
    "Which products have low inventory?",
    "What products are nearly out of stock?",
    "Which products are almost out of stock?",
    "Which products are out of stock?",
    "What items need immediate restocking?",
    "Which products need restocking?",
    "Which products need replenishment?",
    "Which products need immediate replenishment?",
    "Which products are running out?",
    "Show me low stock products.",
    "Show me products with low inventory.",
    "Which shirts are low in stock?",
    "Which jeans are low in stock?",
    "Which sarees are low in stock?",
    "Which pants are low in stock?",
    "Which kurtis are low in stock?",
    "Which dresses are low in stock?",

    # ======================================================
    # HIGH STOCK
    # ======================================================

    "Which products have the highest stock?",
    "Which products have the most stock?",
    "Which products have high stock?",
    "Which products have high inventory?",
    "Which items have the largest stock?",
    "Show me products with high stock.",
    "What products have maximum inventory?",
    "Which products are heavily stocked?",

    # ======================================================
    # OVERSTOCK
    # ======================================================

    "Which products are overstocked?",
    "Which products have excess stock?",
    "Which products have too much stock?",
    "Which products have excess inventory?",
    "What products are over stocked?",
    "Where do I have excess inventory?",
    "Which items should I reduce stock for?",

    # ======================================================
    # PURCHASE / ORDER / REORDER
    # ======================================================

    "What products should I order?",
    "Which products should I order?",
    "Which shirt should I order?",
    "Which shirts should I order?",
    "Which jeans should I order?",
    "Which sarees should I order?",
    "Which product should I order?",
    "What should I order?",
    "What do I need to order?",
    "What do I have to order?",
    "What products do I need to order?",
    "Which products do I need to order?",
    "Which products do I have to order?",
    "What should I buy?",
    "What products should I buy?",
    "Which products should I buy?",
    "Which shirt should I buy?",
    "Which shirts should I buy?",
    "What should I purchase?",
    "Which products should I purchase?",
    "Which products do I need to purchase?",
    "Which products need to be purchased?",
    "What should I reorder?",
    "Which products should I reorder?",
    "Which shirts should I reorder?",
    "Which products need reordering?",
    "Which products need replenishment?",
    "Which products need replenishing?",
    "Which products need restocking?",
    "What should I restock?",
    "What should I replenish?",
    "Which products should I stock up on?",
    "What should I buy now?",
    "What should I purchase now?",
    "What should I order now?",
    "What should I order this week?",
    "What should I purchase this month?",
    "Which products need urgent replenishment?",
    "Which products should I purchase more of?",
    "Which products should I stop purchasing?",
    "Which products need to be reordered?",
    "Which products need to be bought again?",
    "What inventory should I replenish?",
    "What stock should I replenish?",
    "Which stock should I reorder?",
    "Which items should I order next?",
    "Which products should I order next?",
    "Which products should I buy for my shop?",
    "What products should I buy for my shop?",

    # Natural-language purchase questions
    "Which shirt I have to order?",
    "Which shirt do I have to order?",
    "Which shirt do I need to order?",
    "Which shirt should I order?",
    "What shirt should I order?",
    "What shirts do I need to order?",
    "Which shirts do I need?",
    "Which shirt needs ordering?",
    "Which shirts need ordering?",
    "What do I need to buy?",
    "What do I have to buy?",
    "Which products do I need?",
    "What should I get for the shop?",
    "Which products should I get?",
    "Tell me what I should order.",
    "Tell me what I need to reorder.",
    "Can you tell me what to buy?",
    "Can you tell me what I should order?",
    "Help me decide what to order.",
    "Help me decide what to buy.",
    "What stock should I buy?",
    "Which stock should I order?",

    # ======================================================
    # PRICE
    # ======================================================

    "Which product is costly?",
    "Which product is expensive?",
    "Which product is most expensive?",
    "Which product is costliest?",
    "Which shirt is costly?",
    "Which shirt is expensive?",
    "Which shirts are most expensive?",
    "Which products have the highest price?",
    "Which products have the lowest price?",
    "Which product is cheapest?",
    "Which shirt is cheapest?",
    "Which products are cheapest?",
    "What is the cheapest product?",
    "What is the most expensive product?",
    "Which product has the highest MRP?",
    "Which product has the lowest MRP?",
    "What is the selling price?",
    "What is the purchase price?",
    "Show me product prices.",
    "Show me selling prices.",
    "Show me purchase prices.",
    "How much does this product cost?",
    "How much is this shirt?",
    "How much does this shirt cost?",
    "What is the price of this product?",
    "What does this product sell for?",
    "Which products have the highest cost?",
    "Which products have the lowest cost?",

    # ======================================================
    # BRAND
    # ======================================================

    "Which brand is performing best?",
    "Which brand is performing poorly?",
    "Which brand moved fastest?",
    "Which brand sells the most?",
    "Which brand sells the most shirts?",
    "Which brand sells the most jeans?",
    "Which brand sells the most sarees?",
    "Which brand has the highest sales?",
    "Which brand has the lowest sales?",
    "Which brand is most popular?",
    "Which brand has the best sales?",
    "Which brand is selling well?",
    "Which brand is not performing well?",
    "Compare different brands.",
    "Compare my brands.",
    "Show me brand sales.",
    "Show me brand performance.",
    "Which brand should I focus on?",
    "Which brand should I buy more?",

    # ======================================================
    # CATEGORY
    # ======================================================

    "Which category is performing best?",
    "Which category sells the most?",
    "Which category sells the least?",
    "Which category has the highest sales?",
    "Which category has the lowest sales?",
    "Compare my categories.",
    "Compare shirt and jeans sales.",
    "Compare shirts and sarees.",
    "Compare jeans and pants.",
    "How are my shirt sales?",
    "How are my jeans sales?",
    "How are my saree sales?",
    "How are my pant sales?",
    "How are my kurti sales?",
    "How are my dress sales?",
    "Show me category sales.",
    "Which category is most popular?",
    "Which category is selling well?",
    "Which category is weak?",
    "Which category should I focus on?",

    # ======================================================
    # TREND
    # ======================================================

    "Show me the sales trend.",
    "What is my sales trend?",
    "Which products are growing in sales?",
    "Which products are declining?",
    "Which products are improving?",
    "Which products are losing sales?",
    "Are sales increasing?",
    "Are sales decreasing?",
    "Are my sales growing?",
    "Are my sales declining?",
    "Is my business growing?",
    "Is my business declining?",
    "Show me sales growth.",
    "Show me sales decline.",
    "What is the current sales trend?",
    "Which brand has the best sales trend?",
    "Which category has the best trend?",
    "What products are trending?",
    "Which products are becoming popular?",
    "Which products are losing popularity?",

    # ======================================================
    # PROMOTION
    # ======================================================

    "Which products should I promote?",
    "Which products should I advertise?",
    "Which products need promotion?",
    "Which products need advertising?",
    "Which products should I promote this week?",
    "Which products should I promote today?",
    "Which slow products should I promote?",
    "What products should I advertise?",
    "What should I promote?",
    "Which products need marketing?",
    "What products should I market?",

    # ======================================================
    # DISCOUNT
    # ======================================================

    "Which products should I discount?",
    "Which products need a discount?",
    "Which products should I offer discounts on?",
    "Which products should I put on sale?",
    "Which slow products should I discount?",
    "What products should I discount this week?",
    "What products should I put on offer?",
    "Which products need an offer?",
    "Which products should have a price reduction?",

    # ======================================================
    # BUSINESS SUMMARY
    # ======================================================

    "Give me a business summary.",
    "Give me today's business summary.",
    "Give me my business overview.",
    "Give me a business overview.",
    "Give me a sales summary.",
    "Give me an overall summary.",
    "How is my business doing?",
    "How is my shop doing?",
    "How is my textile business doing?",
    "Give me a complete business report.",
    "Give me a business report.",
    "What is happening in my business?",
    "Give me an overall business analysis.",
    "What should I focus on?",
    "What products need attention?",
    "Which products require attention?",
    "What should I focus on this week?",

    # ======================================================
    # STOCK STRATEGY
    # ======================================================

    "Which products should I keep more stock of?",
    "Which products should I reduce stock of?",
    "Which products should I stock more?",
    "Which products should I stock less?",
    "What products should I keep more inventory of?",
    "What products should I reduce inventory of?",

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
    "What should I purchase within ₹100000?",
    "What can I buy with ₹50000?",
    "What can I purchase with ₹100000?",
    "How should I spend my purchase budget?",
    "Help me plan my purchase within ₹50000.",
    "Help me buy stock within ₹100000."
]


# ==========================================================
# INPUT UI
# ==========================================================

if input_mode == "✍️ Custom Question":

    st.markdown(
        "✍️ **Type your own business question**"
    )

    custom_question = st.text_input(
        "Custom Question",
        placeholder=(
            "Example: Which shirt should I order?"
        ),
        label_visibility="collapsed",
        key="custom_question"
    )

    st.info(
        "✍️ Custom Question mode: "
        "Ask your question naturally."
    )

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
        "📋 Example Question mode."
    )


# ==========================================================
# BUTTONS
# ==========================================================

col1, col2 = st.columns(2)


with col1:

    analyse_button = st.button(
        "🔍 Analyse",
        type="primary",
        use_container_width=True
    )


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

        custom_text = (
            st.session_state.custom_question.strip()
        )

        if custom_text:

            question = custom_text

        else:

            st.warning(
                "⚠️ Please type your business question."
            )

    # ------------------------------------------------------
    # EXAMPLE QUESTION
    # ------------------------------------------------------

    else:

        selected_text = (
            st.session_state.selected_example
        )

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
# TEXT NORMALIZATION
# ==========================================================

def normalize_question(question):

    q = str(question).lower().strip()

    # Common apostrophe variations
    q = q.replace("’", "'")
    q = q.replace("`", "'")

    # Common spelling variations
    replacements = {

        "re-order": "reorder",
        "re ordering": "reordering",
        "re order": "reorder",

        "restocking": "restock",
        "restocking": "restock",

        "replenishing": "replenish",
        "replenishment": "replenish",

        "purchasing": "purchase",

        "buying": "buy",

        "advertisement": "advertise",
        "advertising": "advertise",

        "promotions": "promotion",

        "discounts": "discount",

        "inventories": "inventory",

        "t shirts": "t-shirt",
        "tee shirts": "t-shirt",
        "tee shirt": "t-shirt",
        "tees": "t-shirt"
    }

    for old, new in replacements.items():

        q = q.replace(old, new)

    # Remove extra spaces
    q = re.sub(
        r"\s+",
        " ",
        q
    )

    return q


# ==========================================================
# WORD / PHRASE HELPER
# ==========================================================

def contains_any(q, phrases):

    for phrase in phrases:

        phrase = phrase.lower().strip()

        if " " in phrase or "-" in phrase:

            if phrase in q:
                return True

        else:

            if re.search(
                rf"\b{re.escape(phrase)}\b",
                q
            ):
                return True

    return False


# ==========================================================
# PERIOD EXTRACTION
# ==========================================================

def extract_period(q):

    # Default
    period_days = 30

    # Explicit days
    match = re.search(
        r"(?:last|past|previous|for)\s+(\d+)\s+days?",
        q
    )

    if match:

        return int(
            match.group(1)
        )

    # Weeks
    match = re.search(
        r"(?:last|past|previous|for)\s+(\d+)\s+weeks?",
        q
    )

    if match:

        return int(
            match.group(1)
        ) * 7

    # Months
    match = re.search(
        r"(?:last|past|previous|for)\s+(\d+)\s+months?",
        q
    )

    if match:

        return int(
            match.group(1)
        ) * 30

    # Natural periods

    if contains_any(
        q,
        [
            "yesterday",
            "yday"
        ]
    ):

        return 1

    if contains_any(
        q,
        [
            "today",
            "today's"
        ]
    ):

        return 1

    if contains_any(
        q,
        [
            "last week",
            "past week",
            "previous week",
            "this week",
            "weekly"
        ]
    ):

        return 7

    if contains_any(
        q,
        [
            "fortnight",
            "two weeks",
            "last two weeks",
            "past two weeks"
        ]
    ):

        return 14

    if contains_any(
        q,
        [
            "last month",
            "past month",
            "previous month",
            "this month",
            "monthly"
        ]
    ):

        return 30

    if contains_any(
        q,
        [
            "last quarter",
            "past quarter",
            "this quarter",
            "quarter"
        ]
    ):

        return 90

    if contains_any(
        q,
        [
            "last 6 months",
            "past 6 months"
        ]
    ):

        return 180

    if contains_any(
        q,
        [
            "last year",
            "past year",
            "previous year",
            "this year",
            "yearly"
        ]
    ):

        return 365

    if contains_any(
        q,
        [
            "ytd",
            "year to date"
        ]
    ):

        return 365

    return period_days


# ==========================================================
# CATEGORY EXTRACTION
# ==========================================================

def extract_category(question):

    q = normalize_question(question)

    categories = {

        # T-shirt
        "t-shirt": "T-Shirt",
        "t-shirts": "T-Shirt",
        "tee": "T-Shirt",
        "tees": "T-Shirt",

        # Shirt
        "shirts": "Shirt",
        "shirt": "Shirt",

        # Jeans
        "jeans": "Jeans",
        "jean": "Jeans",

        # Pant
        "pants": "Pant",
        "pant": "Pant",
        "trousers": "Pant",
        "trouser": "Pant",

        # Kurti
        "kurtis": "Kurti",
        "kurti": "Kurti",

        # Saree
        "sarees": "Saree",
        "saree": "Saree",

        # Dress
        "dresses": "Dress",
        "dress": "Dress",

        # Top
        "tops": "Top",
        "top": "Top",

        # Jacket
        "jackets": "Jacket",
        "jacket": "Jacket",

        # Skirt
        "skirts": "Skirt",
        "skirt": "Skirt",

        # Kids
        "kidswear": "Kidswear",
        "kids wear": "Kidswear",
        "children wear": "Kidswear",
        "children's wear": "Kidswear",

        # General
        "clothes": None,
        "clothing": None,
        "apparel": None,
        "garments": None,
        "garment": None,
        "products": None,
        "product": None,
        "items": None,
        "item": None
    }

    # Longer phrases first
    keywords = sorted(
        categories.keys(),
        key=len,
        reverse=True
    )

    for keyword in keywords:

        if " " in keyword or "-" in keyword:

            if keyword in q:

                return categories[keyword]

        else:

            if re.search(
                rf"\b{re.escape(keyword)}\b",
                q
            ):

                return categories[keyword]

    return None


# ==========================================================
# BRAND EXTRACTION
# ==========================================================

def extract_brand(question):

    if (
        not data_loaded
        or
        "Brand" not in products_df.columns
    ):

        return None

    q = normalize_question(question)

    brands = (
        products_df["Brand"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    # Longest brands first
    brands = sorted(
        brands,
        key=len,
        reverse=True
    )

    for brand in brands:

        brand_clean = brand.strip().lower()

        if brand_clean and brand_clean in q:

            return brand

    return None


# ==========================================================
# INTENT DETECTION
# ==========================================================

def detect_intent(q):

    # ------------------------------------------------------
    # 1. BUDGET
    # Highest priority when money limit is explicitly given
    # ------------------------------------------------------

    has_budget_word = contains_any(
        q,
        [
            "budget",
            "within my budget",
            "within budget",
            "spend",
            "spending limit",
            "purchase limit"
        ]
    )

    has_currency = bool(
        re.search(
            r"(₹|rs\.?|rupees?)\s*[\d,]+",
            q
        )
    )

    if (
        has_budget_word
        or
        (
            has_currency
            and
            contains_any(
                q,
                [
                    "buy",
                    "purchase",
                    "order",
                    "stock",
                    "replenish"
                ]
            )
        )
    ):

        return "budget_recommendation"


    # ------------------------------------------------------
    # 2. DISCOUNT
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "discount",
            "discounted",
            "discounting",
            "price reduction",
            "reduce price",
            "put on sale",
            "offer discount",
            "special offer"
        ]
    ):

        return "discount_recommendation"


    # ------------------------------------------------------
    # 3. PROMOTION
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "promote",
            "promotion",
            "advertise",
            "advertisement",
            "marketing",
            "market this",
            "run promotion",
            "run an ad"
        ]
    ):

        return "promotion_recommendation"


    # ------------------------------------------------------
    # 4. PRICE
    # ------------------------------------------------------

    # Explicit price questions
    if contains_any(
        q,
        [
            "selling price",
            "purchase price",
            "mrp",
            "price of",
            "cost of",
            "how much",
            "what is the price",
            "what does it cost",
            "what does this cost",
            "price",
            "cost",
            "costly",
            "costliest",
            "expensive",
            "most expensive",
            "cheapest",
            "least expensive",
            "highest price",
            "lowest price",
            "highest cost",
            "lowest cost",
            "maximum price",
            "minimum price"
        ]
    ):

        return "price_analysis"


    # ------------------------------------------------------
    # 5. PURCHASE / ORDER
    #
    # IMPORTANT:
    # This comes BEFORE general sales.
    #
    # This fixes:
    #
    # "which shirt I have to order?"
    # "which shirt should I buy?"
    # "what do I need to reorder?"
    # ------------------------------------------------------

    purchase_action = contains_any(
        q,
        [
            "order",
            "ordering",
            "reorder",
            "reordering",
            "purchase",
            "purchasing",
            "buy",
            "buying",
            "restock",
            "restocking",
            "replenish",
            "replenishing",
            "stock up",
            "stock-up",
            "top up inventory",
            "refill stock"
        ]
    )

    purchase_question = contains_any(
        q,
        [
            "what should i order",
            "what do i order",
            "what do i need to order",
            "what do i have to order",
            "what should i buy",
            "what do i need to buy",
            "what do i have to buy",
            "what should i purchase",
            "what do i need to purchase",
            "which product should i order",
            "which products should i order",
            "which product do i need to order",
            "which products do i need to order",
            "which shirt should i order",
            "which shirts should i order",
            "which shirt do i need to order",
            "which shirts do i need to order",
            "which product should i buy",
            "which products should i buy",
            "which shirt should i buy",
            "which shirts should i buy",
            "which products need ordering",
            "which products need reordering",
            "which products need restocking",
            "which products need replenishment",
            "which products should i reorder",
            "which products should i restock",
            "which products should i replenish",
            "what should i restock",
            "what should i replenish",
            "what should i reorder",
            "what should i purchase",
            "what should i order now",
            "what should i buy now",
            "what should i purchase now",
            "what should i order next",
            "what should i buy next",
            "which items should i order",
            "which items should i buy"
        ]
    )

    if (
        purchase_action
        or
        purchase_question
    ):

        return "purchase_recommendation"


    # ------------------------------------------------------
    # 6. UNSOLD
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "not sold",
            "did not sell",
            "didn't sell",
            "didnt sell",
            "no sale",
            "no sales",
            "zero sales",
            "unsold",
            "never sold",
            "have not sold",
            "haven't sold",
            "has not sold",
            "hasn't sold"
        ]
    ):

        return "unsold_products"


    # ------------------------------------------------------
    # 7. OVERSTOCK
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "overstock",
            "over stocked",
            "overstocked",
            "too much stock",
            "too much inventory",
            "excess stock",
            "excess inventory",
            "surplus stock",
            "surplus inventory",
            "heavily stocked"
        ]
    ):

        return "overstocked"


    # ------------------------------------------------------
    # 8. LOW STOCK
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "low stock",
            "low on stock",
            "running low",
            "low inventory",
            "stock is low",
            "inventory is low",
            "almost out of stock",
            "nearly out of stock",
            "nearly finished",
            "running out",
            "out of stock",
            "stock shortage",
            "inventory shortage"
        ]
    ):

        return "low_stock"


    # ------------------------------------------------------
    # 9. HIGH STOCK
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "highest stock",
            "highest inventory",
            "most stock",
            "maximum stock",
            "maximum inventory",
            "high stock",
            "high inventory",
            "largest stock",
            "largest inventory"
        ]
    ):

        return "high_stock"


    # ------------------------------------------------------
    # 10. FAST MOVING
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "fastest",
            "fast moving",
            "fast-moving",
            "moving fast",
            "moved fast",
            "moves fast",
            "selling fast",
            "selling quickly",
            "sell quickly",
            "selling fastest",
            "best selling",
            "best-selling",
            "top selling",
            "top-selling",
            "most sold",
            "sold the most",
            "sell the most",
            "highest sales",
            "strongest sales",
            "strong demand",
            "high demand",
            "best movers",
            "moving quickly"
        ]
    ):

        return "fast_moving"


    # ------------------------------------------------------
    # 11. SLOW MOVING
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "slow moving",
            "slow-moving",
            "moving slowly",
            "moves slowly",
            "slow selling",
            "slow-selling",
            "selling slowly",
            "sell slowly",
            "poor selling",
            "poor sellers",
            "weak sellers",
            "weak sales",
            "lowest sales",
            "sold the least",
            "least sold",
            "not moving well",
            "stuck in inventory",
            "poor performers",
            "underperforming products"
        ]
    ):

        return "slow_moving"


    # ------------------------------------------------------
    # 12. TREND
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "trend",
            "trending",
            "growing",
            "growth",
            "declining",
            "decline",
            "increasing",
            "increase",
            "decreasing",
            "decrease",
            "improving",
            "improvement",
            "losing sales",
            "falling sales",
            "rising sales",
            "sales growth",
            "sales decline",
            "sales direction",
            "becoming popular",
            "losing popularity"
        ]
    ):

        return "trend_analysis"


    # ------------------------------------------------------
    # 13. BRAND
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "brand",
            "brands",
            "which label",
            "which labels"
        ]
    ):

        return "brand_analysis"


    # ------------------------------------------------------
    # 14. CATEGORY
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "category",
            "categories",
            "compare categories",
            "compare shirt and jeans",
            "compare shirts and sarees",
            "compare jeans and pants"
        ]
    ):

        return "category_analysis"


    # ------------------------------------------------------
    # 15. BUSINESS SUMMARY
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "business summary",
            "business overview",
            "business report",
            "overall summary",
            "overall report",
            "overall business",
            "business performance",
            "how is my business",
            "how is my shop",
            "how is my textile business",
            "what is happening in my business",
            "what should i focus on",
            "products need attention",
            "products require attention"
        ]
    ):

        return "business_summary"


    # ------------------------------------------------------
    # 16. GENERAL SALES
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "sales",
            "sale",
            "sold",
            "selling",
            "units sold",
            "how many sold",
            "how much sold",
            "sales performance",
            "sales amount",
            "sales value",
            "revenue",
            "turnover"
        ]
    ):

        return "sales_summary"


    # ------------------------------------------------------
    # DEFAULT
    # ------------------------------------------------------

    return "sales_summary"


# ==========================================================
# METRIC EXTRACTION
# ==========================================================

def extract_metric(q):

    # Revenue / money
    if contains_any(
        q,
        [
            "revenue",
            "sales value",
            "sales amount",
            "turnover",
            "money",
            "earnings"
        ]
    ):

        return "revenue"

    # Profit
    if contains_any(
        q,
        [
            "profit",
            "profits",
            "margin",
            "profit margin"
        ]
    ):

        return "profit"

    # Price
    if contains_any(
        q,
        [
            "price",
            "cost",
            "mrp"
        ]
    ):

        return "price"

    # Default
    return "units"


# ==========================================================
# BUDGET EXTRACTION
# ==========================================================

def extract_budget(q):

    patterns = [

        # ₹50,000
        r"₹\s*([\d,]+(?:\.\d+)?)",

        # Rs 50,000
        r"\brs\.?\s*([\d,]+(?:\.\d+)?)",

        # 50,000 rupees
        r"([\d,]+(?:\.\d+)?)\s*rupees?",

        # budget 50000
        r"budget\s*(?:of|is|around|up to|upto)?\s*₹?\s*([\d,]+(?:\.\d+)?)",

        # within 50000
        r"within\s+(?:a\s+)?budget\s+(?:of\s+)?₹?\s*([\d,]+(?:\.\d+)?)",

        # spend 50000
        r"spend\s+₹?\s*([\d,]+(?:\.\d+)?)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            q
        )

        if match:

            try:

                return float(
                    match.group(1).replace(
                        ",",
                        ""
                    )
                )

            except Exception:

                return None

    # Currency symbol attached to a number
    match = re.search(
        r"₹?\s*([\d,]+)\s*(?:budget|rupees)",
        q
    )

    if match:

        try:

            return float(
                match.group(1).replace(
                    ",",
                    ""
                )
            )

        except Exception:

            pass

    return None


# ==========================================================
# QUERY UNDERSTANDING
# ==========================================================

def understand_question(question):

    # ------------------------------------------------------
    # Normalize
    # ------------------------------------------------------

    q = normalize_question(
        question
    )


    # ------------------------------------------------------
    # PERIOD
    # ------------------------------------------------------

    period_days = extract_period(
        q
    )


    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    category = extract_category(
        q
    )


    # ------------------------------------------------------
    # INTENT
    # ------------------------------------------------------

    intent = detect_intent(
        q
    )


    # ------------------------------------------------------
    # METRIC
    # ------------------------------------------------------

    metric = extract_metric(
        q
    )


    # ------------------------------------------------------
    # BUDGET
    # ------------------------------------------------------

    budget = extract_budget(
        q
    )


    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    brand = extract_brand(
        q
    )


    # ------------------------------------------------------
    # RETURN
    # ------------------------------------------------------

    return {

        "question": question,

        "query": q,

        "intent": intent,

        "category": category,

        "period_days": period_days,

        "metric": metric,

        "budget": budget,

        "brand": brand
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

        "Sales_Quantity",

        "Sales Quantity",

        "Units Sold"
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

        "Transaction_Date",

        "Sale Date",

        "Transaction Date"
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

        "Product_Name ",

        "Product Name"
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

        "Available_Stock",

        "Available Stock"
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
# GENERAL DATA CLEANING HELPERS
# ==========================================================

def clean_numeric_column(
    df,
    column
):

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        ).fillna(0)

    return df


# ==========================================================
# PREPARE SALES DATA
# ==========================================================

def prepare_sales_data():

    df = sales_df.copy()

    date_column = find_date_column(
        df
    )

    if date_column:

        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )

    quantity_column = find_quantity_column(
        df
    )

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

    date_column = find_date_column(
        df
    )

    # ------------------------------------------------------
    # DATE FILTER
    # ------------------------------------------------------

    if date_column:

        df = df.dropna(
            subset=[date_column]
        )

        if not df.empty:

            latest_date = df[
                date_column
            ].max()

            period_days = max(
                int(info.get("period_days", 30)),
                1
            )

            start_date = (
                latest_date
                -
                pd.Timedelta(
                    days=period_days - 1
                )
            )

            df = df[
                df[date_column] >= start_date
            ]

    # ------------------------------------------------------
    # CATEGORY FILTER
    # ------------------------------------------------------

    category = info.get(
        "category"
    )

    if (
        category
        and
        "Category" in df.columns
    ):

        df = df[
            df["Category"]
            .astype(str)
            .str.strip()
            .str.lower()
            ==
            category.lower()
        ]

    # ------------------------------------------------------
    # BRAND FILTER
    # ------------------------------------------------------

    brand = info.get(
        "brand"
    )

    if (
        brand
        and
        "Brand" in df.columns
    ):

        df = df[
            df["Brand"]
            .astype(str)
            .str.strip()
            .str.lower()
            ==
            brand.lower()
        ]

    return df


# ==========================================================
# MERGE PRODUCT INFORMATION
# ==========================================================

def merge_product_information(df):

    df = df.copy()

    if (
        "Product_ID" in df.columns
        and
        "Product_ID" in products_df.columns
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

        product_data = (
            products_df[
                product_columns
            ]
            .drop_duplicates(
                subset=["Product_ID"]
            )
        )

        df = df.merge(
            product_data,
            on="Product_ID",
            how="left",
            suffixes=(
                "",
                "_product"
            )
        )

    return df


# ==========================================================
# APPLY CATEGORY FILTER
# ==========================================================

def filter_products_by_category(
    df,
    category
):

    df = df.copy()

    if (
        category
        and
        "Category" in df.columns
    ):

        df = df[
            df["Category"]
            .astype(str)
            .str.strip()
            .str.lower()
            ==
            category.lower()
        ]

    return df


# ==========================================================
# FILTER BY BRAND
# ==========================================================

def filter_by_brand(
    df,
    brand
):

    df = df.copy()

    if (
        brand
        and
        "Brand" in df.columns
    ):

        df = df[
            df["Brand"]
            .astype(str)
            .str.strip()
            .str.lower()
            ==
            brand.lower()
        ]

    return df


# ==========================================================
# SALES SUMMARY
# ==========================================================

def sales_summary(info):

    df = filter_sales_data(
        info
    )

    quantity_column = find_quantity_column(
        df
    )

    product_column = find_product_column(
        df
    )

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

    if df.empty:

        return {
            "type": "table",
            "title":
                "📊 Sales Summary",
            "data":
                pd.DataFrame(),
            "message":
                "No sales records were found "
                "for the selected period."
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

    grouped = grouped.head(
        10
    )

    return {

        "type": "table",

        "title":
            f"📊 Top Selling Products — "
            f"Last {info['period_days']} Days",

        "data":
            grouped,

        "message":
            "Here are the products with the "
            "highest sales quantity."
    }


# ==========================================================
# FAST MOVING PRODUCTS
# ==========================================================

def fast_moving_products(info):

    df = filter_sales_data(
        info
    )

    quantity_column = find_quantity_column(
        df
    )

    product_column = find_product_column(
        df
    )

    if (
        quantity_column is None
        or
        product_column is None
    ):

        return {
            "type": "error",
            "message":
                "Required sales columns "
                "were not found."
        }

    if df.empty:

        return {
            "type": "table",
            "title":
                "🔥 Fast-Moving Products",
            "data":
                pd.DataFrame(),
            "message":
                "No sales records were found "
                "for this question."
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

        "data":
            result,

        "message":
            "These products have the strongest "
            "sales movement."
    }


# ==========================================================
# SLOW MOVING PRODUCTS
# ==========================================================

def slow_moving_products(info):

    df = filter_sales_data(
        info
    )

    quantity_column = find_quantity_column(
        df
    )

    product_column = find_product_column(
        df
    )

    if (
        quantity_column is None
        or
        product_column is None
    ):

        return {
            "type": "error",
            "message":
                "Required sales columns "
                "were not found."
        }

    if df.empty:

        return {
            "type": "table",
            "title":
                "🐢 Slow-Moving Products",
            "data":
                pd.DataFrame(),
            "message":
                "No sales records were found."
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

        "data":
            result,

        "message":
            "These products have the lowest "
            "sales movement."
    }


# ==========================================================
# UNSOLD PRODUCTS
# ==========================================================

def unsold_products(info):

    sales = filter_sales_data(
        info
    )

    if "Product_ID" not in sales.columns:

        return {
            "type": "error",
            "message":
                "Product_ID is required to "
                "identify unsold products."
        }

    if "Product_ID" not in products_df.columns:

        return {
            "type": "error",
            "message":
                "Product_ID is missing from "
                "products data."
        }

    sold_ids = set(
        sales[
            "Product_ID"
        ]
        .astype(str)
        .str.strip()
    )

    result = products_df[
        ~products_df[
            "Product_ID"
        ]
        .astype(str)
        .str.strip()
        .isin(
            sold_ids
        )
    ].copy()

    result = filter_products_by_category(
        result,
        info.get("category")
    )

    result = filter_by_brand(
        result,
        info.get("brand")
    )

    return {

        "type": "table",

        "title":
            f"🚫 Products Not Sold — "
            f"Last {info['period_days']} Days",

        "data":
            result,

        "message":
            f"{len(result)} products had "
            f"no sales during the selected period."
    }


# ==========================================================
# INVENTORY HELPER
# ==========================================================

def inventory_with_products():

    df = inventory_df.copy()

    if (
        "Product_ID" in df.columns
        and
        "Product_ID" in products_df.columns
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

        product_data = (
            products_df[
                product_columns
            ]
            .drop_duplicates(
                subset=["Product_ID"]
            )
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

    stock_column = find_stock_column(
        df
    )

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df = clean_numeric_column(
        df,
        stock_column
    )

    result = df[
        df[stock_column] <= 10
    ].copy()

    result = filter_products_by_category(
        result,
        info.get("category")
    )

    result = filter_by_brand(
        result,
        info.get("brand")
    )

    result = result.sort_values(
        stock_column,
        ascending=True
    )

    return {

        "type": "table",

        "title":
            "🔴 Low Stock Products",

        "data":
            result,

        "message":
            f"{len(result)} products are "
            f"currently running low in stock."
    }


# ==========================================================
# HIGH STOCK
# ==========================================================

def high_stock_products(info):

    df = inventory_with_products()

    stock_column = find_stock_column(
        df
    )

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df = clean_numeric_column(
        df,
        stock_column
    )

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
        info.get("category")
    )

    result = filter_by_brand(
        result,
        info.get("brand")
    )

    return {

        "type": "table",

        "title":
            "📦 Highest Stock Products",

        "data":
            result,

        "message":
            "These products currently have "
            "the highest inventory levels."
    }


# ==========================================================
# OVERSTOCKED PRODUCTS
# ==========================================================

def overstocked_products(info):

    df = inventory_with_products()

    stock_column = find_stock_column(
        df
    )

    if stock_column is None:

        return {
            "type": "error",
            "message":
                "Stock column was not found."
        }

    df = clean_numeric_column(
        df,
        stock_column
    )

    # Current rule:
    # 25 or more units = high inventory

    result = df[
        df[stock_column] >= 25
    ].copy()

    result = filter_products_by_category(
        result,
        info.get("category")
    )

    result = filter_by_brand(
        result,
        info.get("brand")
    )

    result = result.sort_values(
        stock_column,
        ascending=False
    )

    return {

        "type": "table",

        "title":
            "📦 Overstocked Products",

        "data":
            result,

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

    inventory = clean_numeric_column(
        inventory,
        stock_column
    )

    # ------------------------------------------------------
    # LOW STOCK FILTER
    # ------------------------------------------------------

    result = inventory[
        inventory[stock_column] <= 10
    ].copy()

    # ------------------------------------------------------
    # CATEGORY FILTER
    # ------------------------------------------------------

    result = filter_products_by_category(
        result,
        info.get("category")
    )

    # ------------------------------------------------------
    # BRAND FILTER
    # ------------------------------------------------------

    result = filter_by_brand(
        result,
        info.get("brand")
    )

    # ------------------------------------------------------
    # NO MATCH
    # ------------------------------------------------------

    if result.empty:

        return {

            "type": "table",

            "title":
                "🛒 Purchase Recommendation",

            "data":
                result,

            "message":
                "No low-stock products were found "
                "for the selected category or brand."
        }

    # ------------------------------------------------------
    # TARGET STOCK
    # ------------------------------------------------------

    TARGET_STOCK = 30

    result["Suggested_Order"] = (
        TARGET_STOCK
        -
        result[stock_column]
    ).clip(
        lower=0
    )

    # ------------------------------------------------------
    # PURCHASE PRICE
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

        result = clean_numeric_column(
            result,
            purchase_price_column
        )

        result["Estimated_Cost"] = (
            result["Suggested_Order"]
            *
            result[purchase_price_column]
        )

    else:

        result["Estimated_Cost"] = 0


    # ------------------------------------------------------
    # REMOVE ZERO ORDERS
    # ------------------------------------------------------

    result = result[
        result["Suggested_Order"] > 0
    ].copy()


    # ------------------------------------------------------
    # SORT
    # ------------------------------------------------------

    result = result.sort_values(
        "Suggested_Order",
        ascending=False
    )


    # ------------------------------------------------------
    # MESSAGE
    # ------------------------------------------------------

    category_text = (
        info.get("category")
        if info.get("category")
        else "all categories"
    )

    brand_text = (
        info.get("brand")
        if info.get("brand")
        else "all brands"
    )

    return {

        "type": "table",

        "title":
            "🛒 Purchase Recommendation",

        "data":
            result,

        "message":
            f"Recommended products for "
            f"{category_text} / {brand_text}. "
            f"These items are low in stock "
            f"and candidates for replenishment."
    }


# ==========================================================
# PRICE ANALYSIS
# ==========================================================

def price_analysis(info):

    df = products_df.copy()

    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    df = filter_products_by_category(
        df,
        info.get("category")
    )

    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    df = filter_by_brand(
        df,
        info.get("brand")
    )

    price_column = find_price_column(
        df
    )

    if price_column is None:

        return {
            "type": "error",
            "message":
                "No price column was found "
                "in products data."
        }

    df = clean_numeric_column(
        df,
        price_column
    )

    df = df[
        df[price_column] > 0
    ].copy()

    q = info.get(
        "query",
        ""
    ).lower()

    # ------------------------------------------------------
    # EXPENSIVE
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "costly",
            "costliest",
            "expensive",
            "most expensive",
            "highest price",
            "highest cost",
            "maximum price"
        ]
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

            "data":
                result,

            "message":
                f"The highest-priced products "
                f"are shown using {price_column}."
        }


    # ------------------------------------------------------
    # CHEAPEST
    # ------------------------------------------------------

    if contains_any(
        q,
        [
            "cheapest",
            "lowest price",
            "least expensive",
            "lowest cost",
            "minimum price"
        ]
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

            "data":
                result,

            "message":
                f"The lowest-priced products "
                f"are shown using {price_column}."
        }


    # ------------------------------------------------------
    # GENERAL PRICE
    # ------------------------------------------------------

    result = df.head(
        20
    )

    return {

        "type": "table",

        "title":
            "💰 Product Prices",

        "data":
            result,

        "message":
            "Here are the available product prices."
    }


# ==========================================================
# BRAND ANALYSIS
# ==========================================================

def brand_analysis(info):

    sales = filter_sales_data(
        info
    )

    sales = merge_product_information(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        quantity_column is None
        or
        "Brand" not in sales.columns
    ):

        return {
            "type": "error",
            "message":
                "Brand or sales quantity "
                "data was not found."
        }

    if sales.empty:

        return {
            "type": "table",
            "title":
                "🏷️ Brand Sales Performance",
            "data":
                pd.DataFrame(),
            "message":
                "No brand sales were found "
                "for the selected period."
        }

    brand_sales = (
        sales
        .groupby(
            "Brand"
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
            f"🏷️ Brand Sales Performance — "
            f"Last {info['period_days']} Days",

        "data":
            brand_sales,

        "message":
            "Brands are ranked according "
            "to sales quantity."
    }


# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

def category_analysis(info):

    sales = filter_sales_data(
        info
    )

    sales = merge_product_information(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        quantity_column is None
        or
        "Category" not in sales.columns
    ):

        return {
            "type": "error",
            "message":
                "Category or sales quantity "
                "data was not found."
        }

    if sales.empty:

        return {
            "type": "table",
            "title":
                "👕 Category Performance",
            "data":
                pd.DataFrame(),
            "message":
                "No category sales were found."
        }

    category_sales = (
        sales
        .groupby(
            "Category"
        )[quantity_column]
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

        "data":
            category_sales,

        "message":
            "Categories are ranked according "
            "to sales quantity."
    }


# ==========================================================
# TREND ANALYSIS
# ==========================================================

def trend_analysis(info):

    sales = filter_sales_data(
        info
    )

    date_column = find_date_column(
        sales
    )

    quantity_column = find_quantity_column(
        sales
    )

    if (
        date_column is None
        or
        quantity_column is None
    ):

        return {
            "type": "error",
            "message":
                "Date or quantity column "
                "was not found."
        }

    sales = sales.dropna(
        subset=[
            date_column
        ]
    )

    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    if (
        info.get("category")
        and
        "Category" in sales.columns
    ):

        sales = sales[
            sales["Category"]
            .astype(str)
            .str.lower()
            ==
            info["category"].lower()
        ]

    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    if (
        info.get("brand")
        and
        "Brand" in sales.columns
    ):

        sales = sales[
            sales["Brand"]
            .astype(str)
            .str.lower()
            ==
            info["brand"].lower()
        ]

    if sales.empty:

        return {
            "type": "chart",
            "title":
                "📈 Sales Trend",
            "data":
                pd.DataFrame(),
            "date_column":
                date_column,
            "quantity_column":
                quantity_column,
            "message":
                "No data available "
                "to calculate the trend."
        }

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

    # ------------------------------------------------------
    # TREND DIRECTION
    # ------------------------------------------------------

    if len(trend) >= 2:

        first_value = float(
            trend[
                quantity_column
            ].iloc[0]
        )

        last_value = float(
            trend[
                quantity_column
            ].iloc[-1]
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

        "data":
            trend,

        "date_column":
            date_column,

        "quantity_column":
            quantity_column,

        "message":
            direction
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
            "Slow-moving products may benefit "
            "from promotions, bundles or "
            "targeted offers."
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
            "These slower-moving products may "
            "be candidates for a discount strategy."
    }


# ==========================================================
# BUDGET RECOMMENDATION
# ==========================================================

def budget_recommendation(info):

    budget = info.get(
        "budget"
    )

    if budget is None:

        return {

            "type": "error",

            "message":
                "Please specify a budget. "
                "Example: What should I buy "
                "with ₹50,000?"
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
                "Purchase price information "
                "was not found."
        }

    inventory = clean_numeric_column(
        inventory,
        stock_column
    )

    inventory = clean_numeric_column(
        inventory,
        purchase_price_column
    )

    # ------------------------------------------------------
    # LOW STOCK FIRST
    # ------------------------------------------------------

    inventory = inventory[
        inventory[stock_column] <= 10
    ].copy()

    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    inventory = filter_products_by_category(
        inventory,
        info.get("category")
    )

    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    inventory = filter_by_brand(
        inventory,
        info.get("brand")
    )

    # ------------------------------------------------------
    # SUGGESTED ORDER
    # ------------------------------------------------------

    TARGET_STOCK = 30

    inventory["Suggested_Order"] = (
        TARGET_STOCK
        -
        inventory[stock_column]
    ).clip(
        lower=0
    )

    # ------------------------------------------------------
    # COST
    # ------------------------------------------------------

    inventory["Estimated_Cost"] = (
        inventory["Suggested_Order"]
        *
        inventory[purchase_price_column]
    )

    inventory = inventory[
        inventory["Suggested_Order"] > 0
    ].copy()

    # ------------------------------------------------------
    # SORT BY COST
    # ------------------------------------------------------

    inventory = inventory.sort_values(
        "Estimated_Cost",
        ascending=True
    )

    # ------------------------------------------------------
    # SELECT WITHIN BUDGET
    # ------------------------------------------------------

    selected_rows = []

    remaining_budget = float(
        budget
    )

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

        result = inventory.head(
            0
        )

    spent = (
        float(budget)
        -
        remaining_budget
    )

    return {

        "type": "budget",

        "title":
            f"💰 Purchase Plan Within "
            f"₹{budget:,.0f}",

        "data":
            result,

        "budget":
            float(budget),

        "spent":
            spent,

        "remaining":
            remaining_budget,

        "message":
            f"Recommended products within "
            f"your ₹{budget:,.0f} budget."
    }


# ==========================================================
# BUSINESS SUMMARY
# ==========================================================

def business_summary(info):

    sales = filter_sales_data(
        info
    )

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
                "Sales quantity column "
                "was not found."
        }

    total_units = float(
        sales[
            quantity_column
        ].sum()
    )

    low_stock_count = 0

    if stock_column:

        inventory = clean_numeric_column(
            inventory,
            stock_column
        )

        low_stock_count = int(
            (
                inventory[
                    stock_column
                ] <= 10
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

    intent = info.get(
        "intent",
        "sales_summary"
    )

    # ------------------------------------------------------
    # SALES
    # ------------------------------------------------------

    if intent == "sales_summary":

        return sales_summary(
            info
        )

    if intent == "fast_moving":

        return fast_moving_products(
            info
        )

    if intent == "slow_moving":

        return slow_moving_products(
            info
        )


    # ------------------------------------------------------
    # INVENTORY
    # ------------------------------------------------------

    if intent == "unsold_products":

        return unsold_products(
            info
        )

    if intent == "low_stock":

        return low_stock_products(
            info
        )

    if intent == "high_stock":

        return high_stock_products(
            info
        )

    if intent == "overstocked":

        return overstocked_products(
            info
        )


    # ------------------------------------------------------
    # PURCHASE
    # ------------------------------------------------------

    if intent == "purchase_recommendation":

        return purchase_recommendation(
            info
        )


    # ------------------------------------------------------
    # PRICE
    # ------------------------------------------------------

    if intent == "price_analysis":

        return price_analysis(
            info
        )


    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    if intent == "brand_analysis":

        return brand_analysis(
            info
        )


    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    if intent == "category_analysis":

        return category_analysis(
            info
        )


    # ------------------------------------------------------
    # TREND
    # ------------------------------------------------------

    if intent == "trend_analysis":

        return trend_analysis(
            info
        )


    # ------------------------------------------------------
    # PROMOTION
    # ------------------------------------------------------

    if intent == "promotion_recommendation":

        return promotion_recommendation(
            info
        )


    # ------------------------------------------------------
    # DISCOUNT
    # ------------------------------------------------------

    if intent == "discount_recommendation":

        return discount_recommendation(
            info
        )


    # ------------------------------------------------------
    # BUDGET
    # ------------------------------------------------------

    if intent == "budget_recommendation":

        return budget_recommendation(
            info
        )


    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------

    if intent == "business_summary":

        return business_summary(
            info
        )


    # ------------------------------------------------------
    # DEFAULT
    # ------------------------------------------------------

    return sales_summary(
        info
    )


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

        if result.get("message"):

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

        chart_data = result[
            "data"
        ].copy()

        date_column = result[
            "date_column"
        ]

        quantity_column = result[
            "quantity_column"
        ]

        if (
            not chart_data.empty
            and
            date_column in chart_data.columns
            and
            quantity_column in chart_data.columns
        ):

            chart_data = (
                chart_data
                .set_index(
                    date_column
                )
            )

            st.line_chart(
                chart_data[
                    quantity_column
                ]
            )

        else:

            st.info(
                "No chart data is available "
                "for this question."
            )

        return


    # ======================================================
    # BUDGET
    # ======================================================

    if result["type"] == "budget":

        st.success(
            result["message"]
        )

        col1, col2, col3 = st.columns(
            3
        )

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

        col1, col2, col3, col4 = st.columns(
            4
        )

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
                f"{result['low_stock']} "
                f"low-stock products. "
                f"Review replenishment before "
                f"stock runs out."
            )

        else:

            st.info(
                "No products are currently "
                "below the low-stock threshold."
            )

        return


# ==========================================================
# BUSINESS RECOMMENDATION
# ==========================================================

def show_recommendation(
    info,
    result
):

    intent = info[
        "intent"
    ]

    st.markdown(
        "### 💡 Business Recommendation"
    )


    # ------------------------------------------------------
    # FAST MOVING
    # ------------------------------------------------------

    if intent == "fast_moving":

        st.info(
            "🔥 Prioritize these fast-moving "
            "products when planning your "
            "next purchase."
        )


    # ------------------------------------------------------
    # SLOW MOVING
    # ------------------------------------------------------

    elif intent == "slow_moving":

        st.warning(
            "🐢 Consider promotions, bundles "
            "or smaller future purchases "
            "for slow-moving items."
        )


    # ------------------------------------------------------
    # UNSOLD
    # ------------------------------------------------------

    elif intent == "unsold_products":

        st.warning(
            "📢 Consider discounts, bundles "
            "or promotional campaigns for "
            "products with no sales."
        )


    # ------------------------------------------------------
    # LOW STOCK
    # ------------------------------------------------------

    elif intent == "low_stock":

        st.warning(
            "📦 Review these products for "
            "replenishment, especially if "
            "they are also fast-moving."
        )


    # ------------------------------------------------------
    # HIGH STOCK
    # ------------------------------------------------------

    elif intent == "high_stock":

        st.info(
            "📦 Monitor high-stock products "
            "carefully to avoid over-purchasing."
        )


    # ------------------------------------------------------
    # OVERSTOCK
    # ------------------------------------------------------

    elif intent == "overstocked":

        st.warning(
            "📦 These products have relatively "
            "high stock. Consider slowing future "
            "purchases or using promotions."
        )


    # ------------------------------------------------------
    # PURCHASE
    # ------------------------------------------------------

    elif intent == "purchase_recommendation":

        st.success(
            "🛒 Prioritize low-stock products "
            "and compare their recent sales "
            "movement before ordering."
        )


    # ------------------------------------------------------
    # PRICE
    # ------------------------------------------------------

    elif intent == "price_analysis":

        st.info(
            "💰 Use price information together "
            "with sales movement before changing "
            "your product mix."
        )


    # ------------------------------------------------------
    # BRAND
    # ------------------------------------------------------

    elif intent == "brand_analysis":

        st.success(
            "🏷️ Strong-performing brands can "
            "receive more purchasing and "
            "promotional attention."
        )


    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    elif intent == "category_analysis":

        st.success(
            "👕 Focus inventory and purchasing "
            "on categories with stronger demand."
        )


    # ------------------------------------------------------
    # TREND
    # ------------------------------------------------------

    elif intent == "trend_analysis":

        st.info(
            "📈 Use the trend direction to "
            "plan inventory and upcoming purchases."
        )


    # ------------------------------------------------------
    # PROMOTION
    # ------------------------------------------------------

    elif intent == "promotion_recommendation":

        st.warning(
            "📢 Consider promoting slower-moving "
            "products to improve inventory turnover."
        )


    # ------------------------------------------------------
    # DISCOUNT
    # ------------------------------------------------------

    elif intent == "discount_recommendation":

        st.warning(
            "🏷️ Consider targeted discounts "
            "for products that remain slow-moving."
        )


    # ------------------------------------------------------
    # BUDGET
    # ------------------------------------------------------

    elif intent == "budget_recommendation":

        st.success(
            "💰 Prioritize products that need "
            "replenishment while keeping the "
            "purchase within your budget."
        )


    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------

    elif intent == "business_summary":

        st.info(
            "📊 Use the overall business picture "
            "to balance sales, inventory and "
            "future purchases."
        )


    # ------------------------------------------------------
    # DEFAULT
    # ------------------------------------------------------

    else:

        st.info(
            "📊 Review sales, inventory and "
            "purchase movement together "
            "before making a decision."
        )


# ==========================================================
# EXECUTE QUESTION
# ==========================================================

if (
    question
    and
    data_loaded
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

            info["brand"] = (
                detected_brand
            )


            # ----------------------------------------------
            # SHOW QUERY UNDERSTANDING
            # ----------------------------------------------

            with st.expander(
                "🔎 Query Understanding",
                expanded=True
            ):

                col1, col2, col3, col4 = st.columns(
                    4
                )

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

            st.session_state.analysis_result = (
                result
            )


            # ----------------------------------------------
            # DISPLAY RESULT
            # ----------------------------------------------

            display_result(
                result
            )


            # ----------------------------------------------
            # BUSINESS RECOMMENDATION
            # ----------------------------------------------

            if (
                result
                and
                result.get("type") != "error"
            ):

                show_recommendation(
                    info,
                    result
                )


        except Exception as e:

            st.error(
                "❌ Analysis failed."
            )

            st.exception(
                e
            )


# ==========================================================
# NO QUESTION MESSAGE
# ==========================================================

elif (
    not question
    and
    data_loaded
):

    st.info(
        "👆 Choose Custom Question or "
        "Example Question, enter/select "
        "your question and click Analyse."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "🧞 TextileGenie AI — "
    "Rule-Based Textile Business Intelligence"
)
