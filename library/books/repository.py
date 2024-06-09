from sqlalchemy import text

from library.library_marshmallow import BookSchema
from ..extension import db

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def get_all_repo():
    try:
        query = text('''
            SELECT
                b.id,
                b.name,
                b.page_count,
                a.name as author,
                c.name as category
            FROM books b
            LEFT JOIN author a ON b.author_id = a.id
            LEFT JOIN category c ON b.category_id = c.id
        ''')
        books = db.session.execute(query)
        books_list = [dict(row._asdict()) for row in books]
        return books_list
    except Exception as e:
        return None


def add_book_repo(new_book):
    try:
        db.session.add(new_book)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False


def get_book_by_id_repo(book_id):
    try:
        query = text('''
            SELECT
                b.id,
                b.name,
                b.page_count,
                b.author_id,
                b.category_id,
                a.name as author,
                c.name as category
            FROM books b
            LEFT JOIN author a ON b.author_id = a.id
            LEFT JOIN category c ON b.category_id = c.id
            WHERE b.id = :book_id
        ''')
        book = db.session.execute(query, {'book_id': book_id}).fetchone()
        if book:
            return dict(book._asdict())
        return None
    except Exception as e:
        print(e)
        return None


def update_book_repo():
    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False
