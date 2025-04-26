from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = {
    1: {"id": 1, "title": "1984", "author": "George Orwell", "category": "Dystopian"},
    2: {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    3: {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"},
    4: {"id": 4, "title": "Brave New World", "author": "Aldous Huxley", "category": "Dystopian"},
}

@app.get("/books")
def read_root():
    return BOOKS

@app.get("/books/")
def get_by_category(category: str):
    return [book for book in BOOKS.values() if book["category"].lower() == category.lower()]


@app.post("/books/")
def create_book(book: dict = Body()):
    new_id = max(BOOKS.keys()) + 1
    BOOKS[new_id] = book
    BOOKS[new_id]["id"] = new_id

@app.get("/books/by_id/{book_id}")
def read_item(book_id: int):
    return BOOKS.get(book_id, {"error": "Book not found"})

@app.get("/books/by_author/{author}/")
def get_by_author(author: str, category: str = None):
    if category:
        return [book for book in BOOKS.values() if author.lower() in book["author"].lower() and book["category"].lower() == category.lower()]
    else:
        return [book for book in BOOKS.values() if author.lower() in book["author"].lower()]

@app.put("/books/{book_id}")
def update_book(book_id: int, book: dict = Body()):
    if book_id in BOOKS:
        BOOKS[book_id] = book
        BOOKS[book_id]["id"] = book_id
    else:
        return {"error": "Book not found"}

@app.patch("/books/{book_id}")
def partial_update_book(book_id: int, book: dict = Body()):
    if book_id in BOOKS:
        BOOKS[book_id].update(book)
    else:
        return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id in BOOKS:
        del BOOKS[book_id]
    else:
        return {"error": "Book not found"}
