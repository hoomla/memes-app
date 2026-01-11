from pydantic import BaseModel, Field
from typing import Literal


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["rating", "date", "popularity"] = "date"
    tags: list[str] = []
