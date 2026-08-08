# 🧞 TextileGenie AI Chatbot

## AI-Powered Textile Retail Business Assistant

TextileGenie is a **Rule-Based AI Business Intelligence Assistant** designed for textile retail businesses.

It analyzes **product, sales, inventory, and purchase data** and converts business questions into useful data-driven answers, summaries, product rankings, and business recommendations.

The application allows users to either:

- ✍️ Enter their own business question
- 📋 Select from predefined business questions
- 🔍 Analyse the question
- 📊 View the corresponding business analysis
- 💡 Receive a rule-based business recommendation

---

# 🎯 Problem Statement

Textile retailers generate large amounts of business data every day, including:

- Product information
- Sales transactions
- Inventory levels
- Purchase records
- Product pricing
- Product categories
- Brand information

However, many small and medium-sized textile businesses still depend on **manual data checking and spreadsheet analysis** to answer simple but important business questions.

For example:

- Which products are selling fastest?
- Which products are not selling?
- Which products are slow-moving?
- Which products are running low in stock?
- Which products should be reordered?
- Which products are expensive?
- Which brands are performing well?
- What are the recent sales trends?
- Which products generate the highest revenue?
- Which products have the highest profit margin?

Manually answering these questions can be time-consuming and may delay business decisions.

---

# 💡 Solution

TextileGenie provides a simple **rule-based business intelligence layer** over textile retail data.

The system accepts a business question and identifies important information such as:

- **Business intent**
- **Product category**
- **Time period**
- **Business metric**

It then applies predefined business rules to the available datasets and produces a relevant analysis.

### Example

User asks:

> "Which shirt should I order?"

TextileGenie can analyse:

**Products → Sales → Inventory → Purchase Data**

and identify products that may require replenishment.

---

# 🔄 How TextileGenie Works

```text
                USER
                  │
                  ▼
        💬 Business Question
                  │
                  ▼
        🔍 Query Understanding
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Intent   Category   Period
        │         │         │
        └─────────┼─────────┘
                  ▼
          📊 Data Analysis
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
     Sales    Inventory   Purchases
       │          │          │
       └──────────┼──────────┘
                  ▼
          📈 Business Result
                  │
                  ▼
          💡 Recommendation
