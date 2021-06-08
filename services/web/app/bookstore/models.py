from datetime import datetime
from app import db


AUTHOR_NAME = 'First name'
AUTHOR_LAST_NAME = 'Last name'
AUTHOR_BIRTHDAY = 'Birthday'

BOOK_TITLE = 'Title'
BOOK_PRICE = 'Price'
BOOK_YEAR = 'Publication year'
BOOK_ISBN = 'ISBN'


class Author(db.Model):
    """

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(AUTHOR_NAME, db.String(64))
    last_name = db.Column(AUTHOR_LAST_NAME, db.String(64))
    birthday = db.Column(AUTHOR_BIRTHDAY, db.DateTime, default=datetime.now)

    def __init__(self, id, name, last_name, birthday):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.birthday = birthday

    def get_full_name(self):
        return f'{self.name} {self.last_name}'


class Book(db.Model):
    """

    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(BOOK_TITLE, db.String(128))
    price = db.Column(BOOK_PRICE, db.Float)
    isbn = db.Column(BOOK_ISBN, db.Integer, unique=True)
    year = db.Column(BOOK_YEAR, db.DateTime, nullable=True)
