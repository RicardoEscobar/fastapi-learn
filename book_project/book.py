"""This is a book module that contains the Book class."""


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        rating: int,
        published_date: int,
    ) -> None:
        """Initialize a Book instance with the given attributes.

        Args:
            id (int): The ID of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            description (str): A brief description of the book.
            rating (int): The rating of the book.
            published_date (int): The year the book was published.
        """
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
