"""This module contains the find_book_id function that assigns a book ID to a new book."""
from typing import List
from book import Book


def find_book_id(book: Book, books: List[Book]) -> Book:
    """Find the next available book ID.

    Args:
        book (Book): The book object to assign an ID to.
        books (list[Book]): The list of existing books.

    Returns:
        Book: The book object with the assigned ID.
    """
    if len(books) > 0:
        book.id = books[-1].id + 1
    else:
        book.id = 1
    return book
