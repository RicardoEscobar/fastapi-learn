"""This module contains the BookRequest class."""

from typing import Optional
from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed for create.", default=None)
    title: Optional[str] = Field(min_length=3, default="Book title")
    author: Optional[str] = Field(min_length=1, default="Book author")
    description: Optional[str] = Field(min_length=1, max_length=100, default="Book description")
    rating: Optional[int] = Field(ge=1, le=5, default=1)
    published_date: Optional[int] = Field(gt=1999, lt=2031, description="Year of publication", default=2025)

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
