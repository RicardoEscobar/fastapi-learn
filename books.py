from fastapi import FastAPI

from book import Book
from bookrequest import BookRequest
from find_book_id import find_book_id

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A great book!", 5),
    Book(3, "Master Endpoints", "codingwithroby", "An awesome book!", 5),
    Book(4, "HP1", "Author 1", "Book 1 description", 2),
    Book(5, "HP2", "Author 2", "Book 2 description", 3),
    Book(6, "HP3", "Author 3", "Book 3 description", 1),
]

@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/create-book")
async def create_book(book: BookRequest):
    new_book = Book(**book.model_dump())
    new_book = find_book_id(new_book, BOOKS)
    BOOKS.append(new_book)
