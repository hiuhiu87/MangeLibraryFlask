from flask import Blueprint

from library.books.service import *
from library.constants import API_PREFIX_BOOKS

books = Blueprint('books', __name__, url_prefix=API_PREFIX_BOOKS)


@books.route(rule='/', methods=['GET'])
def get_all_request():
    return get_all()


@books.route(rule='/', methods=['POST'])
def add_books_request():
    return add_books()


@books.route(rule='/<int:book_id>', methods=['GET'])
def get_book_by_id_request(book_id):
    return get_book_by_id(book_id)


@books.route(rule='/<int:book_id>', methods=['PUT'])
def update_book_request(book_id):
    return update_book(book_id)
