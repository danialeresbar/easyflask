from datetime import datetime
from ..app import database


AUTHOR_NAME = 'First name'
AUTHOR_LAST_NAME = 'Last name'
AUTHOR_BIRTHDAY = 'Birthday'

BOOK_TITLE = 'Title'
BOOK_PRICE = 'Price'
BOOK_YEAR = 'Publication year'
BOOK_ISBN = 'ISBN'


class Author(database.Model):
    """

    """

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(AUTHOR_NAME, database.String(64))
    last_name = database.Column(AUTHOR_LAST_NAME, database.String(64))
    birthday = database.Column(AUTHOR_BIRTHDAY, database.DateTime, default=datetime.now)

    def get_full_name(self):
        return f'{self.name} {self.last_name}'


class Book(database.Model):
    """

    """

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(BOOK_TITLE, database.String(128))
    price = database.Column(BOOK_PRICE, database.Float)
    isbn = database.Column(BOOK_ISBN, database.Integer, unique=True)
    year = database.Column(BOOK_YEAR, database.DateTime, nullable=True)
