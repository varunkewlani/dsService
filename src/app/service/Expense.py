from typing import Optional

# NOTE: langchain-core 0.1.x / langchain-mistralai 0.1.2 only recognise a schema as
# a "pydantic schema" when it subclasses langchain_core.pydantic_v1.BaseModel.
# Using pydantic v2's BaseModel here makes `is_pydantic_schema` False inside
# `with_structured_output`, which then builds an EMPTY tool schema ("properties": {})
# and returns a bare dict -> amount/merchant/currency never get populated.
from langchain_core.pydantic_v1 import BaseModel, Field


class Expense(BaseModel):
    """Information about a transaction made on any Card"""

    amount: Optional[str] = Field(
        default=None, description="Amount / value of the transaction"
    )
    merchant: Optional[str] = Field(
        default=None, description="Merchant name to whom the transaction was made"
    )
    currency: Optional[str] = Field(
        default=None, description="Currency of the transaction"
    )

    def serialize(self):
        return {
            "amount": self.amount,
            "merchant": self.merchant,
            "currency": self.currency,
        }
