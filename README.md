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

The Rule-Based TextileGenie AI Chatbot has several strong advantages, especially for a small or medium-sized textile retail business.

🧞 Main Advantages

| Advantage                    | What it means for TextileGenie                                                                      |
| ---------------------------- | --------------------------------------------------------------------------------------------------- |
| ⚡ **Fast**                   | Answers business questions quickly because it uses predefined rules and data processing.            |
| 🎯 **Predictable**           | The same question with the same data produces consistent results.                                   |
| 💰 **Low Cost**              | No LLM/Groq API cost is required for the current version.                                           |
| 🔒 **Data Privacy**          | Business data can be processed directly without sending it to an external LLM.                      |
| 📶 **Lightweight**           | It doesn't need a large AI model or GPU.                                                            |
| 🧮 **Accurate Calculations** | Sales, stock, prices and quantities come directly from the CSV data and deterministic calculations. |
| 🛠️ **Easy to Maintain**     | Business rules can be changed directly in Python.                                                   |
| 🚀 **Easy Deployment**       | Streamlit + Python + CSV files is relatively simple to deploy.                                      |
| 🔍 **Explainable**           | You can clearly explain why a particular product was recommended.                                   |
| 📊 **Business-Focused**      | It concentrates specifically on sales, inventory, purchases, pricing and product performance.       |

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
