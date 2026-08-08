from typing import TypedDict, Any


class TextileState(TypedDict, total=False):

    question: str

    intent: str
    category: str
    brand: str
    period_days: int
    metric: str

    products_df: Any
    sales_df: Any
    inventory_df: Any
    purchase_df: Any

    analysis: dict
    inventory_result: Any
    purchase_result: Any

    trend: Any
    forecast: dict

    insights: list
    recommendations: list

    validation: dict

    final_answer: str
