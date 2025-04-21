"""This module contains the BookRequest class."""

from typing import Optional
from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed for create.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book.",
                "rating": 5,
            }
        }
    }
