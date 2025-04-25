from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status

from book import Book
from bookrequest import BookRequest
from find_book_id import find_book_id

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 2023),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A great book!", 5, 2023),
    Book(3, "Master Endpoints", "codingwithroby", "An awesome book!", 5, 2025),
    Book(4, "HP1", "Author 1", "Book 1 description", 2, 2025),
    Book(5, "HP2", "Author 2", "Book 2 description", 3, 2027),
    Book(6, "HP3", "Author 3", "Book 3 description", 1, 2027),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating_and_published_date(
    published_date: int = Query(gt=1999, lt=2031), rating: int = Query(qt=0, lt=6)
):
    filtered_books = BOOKS.copy()
    if rating:
        filtered_books = [book for book in filtered_books if book.rating == rating]
    if published_date:
        filtered_books = [
            book for book in filtered_books if book.published_date == published_date
        ]
    if filtered_books:
        return filtered_books
    else:
        return {
            "error": f"No books found with the given rating: {rating} and published date: {published_date}"
        }


@app.get("/books/published/", status_code=status.HTTP_200_OK)
async def get_books_by_published_date(
    published_date: int = Query(gt=1999, lt=2031),
    gt: int = Query(gt=1999),
    lt: int = Query(lt=2031),
):
    filtered_books = BOOKS.copy()

    if published_date:
        filtered_books = [
            book for book in filtered_books if book.published_date == published_date
        ]
    elif gt or lt:

        if gt:
            filtered_books = [
                book for book in filtered_books if book.published_date > gt
            ]
        if lt:
            filtered_books = [
                book for book in filtered_books if book.published_date < lt
            ]

    if filtered_books:
        return filtered_books
    else:
        return {
            "error": f"No books found with the given published date {published_date} or range: {gt} - {lt}"
        }


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookRequest):
    new_book = Book(**book.model_dump())
    new_book = find_book_id(new_book, BOOKS)
    BOOKS.append(new_book)


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = Book(**book.model_dump())
            return
    raise HTTPException(status_code=404, detail="Book not found")


@app.patch("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def patch_book(book: BookRequest):
    for existing_book in BOOKS:
        if existing_book.id == book.id:
            book_data = book.model_dump()
            for key, value in book_data.items():
                # Update only the provided keys and values
                setattr(existing_book, key, value)
            return
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            del BOOKS[i]
            return
    raise HTTPException(status_code=404, detail="Book not found")
