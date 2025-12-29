from typing import List, TypedDict, Literal


Category = Literal["Sales", "Support", "Billing", "Partnership", "Spam", "Other"]
Priority = Literal["High", "Medium", "Low"]


class ClassificationResult(TypedDict):
    category: Category
    priority: Priority
    intent: str
    summary: str
    suggested_response: str
    confidence: float
    needs_human_review: bool
    tags: List[str]
