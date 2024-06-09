from flask import request, jsonify

from .repository import *
from ..models import Books
from ..utils import response_error, response_obj


def get_all():
    try:
        books = get_all_repo()
        if books:
            return response_obj(
                message='Books fetched successfully',
                data=books
            )
        else:
            return response_error(
                message='Error while fetching books',
                status_code=400
            )
    except Exception as e:
        print(e)
        return response_error(
            message='Error while fetching books',
            status_code=400
        )


def add_books():
    try:
        data = request.get_json()
        result = book_schema.load(data)
        new_book = Books(
            name=result['name'],
            page_count=result['page_count'],
            author_id=result['author_id'],
            category_id=result['category_id']
        )
        result_add = add_book_repo(new_book)
        if result_add:
            return response_obj(
                message='Book added successfully',
                data=book_schema.dump(new_book)
            )
        else:
            return response_error(
                message='Error while adding book',
                status_code=400
            )
    except Exception as e:
        return response_error(
            message='Error while adding book',
            data=jsonify(e) if isinstance(e, dict) else str(e),
            status_code=400
        )


def get_book_by_id(book_id):
    try:
        book = get_book_by_id_repo(book_id)
        print(book)
        if book:
            return response_obj(
                message='Book fetched successfully',
                data=book
            )
        else:
            return response_error(
                message='Book not found',
                status_code=400
            )
    except Exception as e:
        return response_error(
            message='Error while fetching book',
            data=jsonify(e) if isinstance(e, dict) else str(e),
            status_code=400
        )


def update_book(book_id):
    try:
        data = request.get_json()
        book = get_book_by_id_repo(book_id)
        if not book:
            return response_error(
                message='Book not found',
                status_code=404
            )
        result = book_schema.load({
            'name': data.get('name', book['name']),
            'page_count': data.get('page_count', book['page_count']),
            'author_id': data.get('author_id', book['author_id']),
            'category_id': data.get('category_id', book['category_id'])
        })
        book['name'] = result['name']
        book['page_count'] = result['page_count']
        book['author_id'] = result['author_id']
        book['category_id'] = result['category_id']
        result_update = update_book_repo()
        if result_update:
            return response_obj(
                message='Book updated successfully',
                data=book_schema.dump(book)
            )
        else:
            return response_error(
                message='Error while updating book',
                status_code=400
            )
    except Exception as e:
        return response_error(
            message='Error while updating book',
            data=jsonify(e) if isinstance(e, dict) else str(e),
            status_code=400
        )
