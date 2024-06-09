from flask import request

from ..extension import db
from library.library_marshmallow import AuthorSchema
from library.models import Author
from library.utils import response_obj, response_error

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


def get_all():
    try:
        authors = Author.query.all()
        return response_obj(
            message='Authors fetched successfully',
            data=authors_schema.dump(authors)
        )
    except Exception as e:
        return response_error(
            message='Error while fetching authors',
            status_code=400
        )


def add_author():
    try:
        data = request.get_json()
        result = author_schema.load(data)
        new_author = Author(
            name=result['name']
        )
        db.session.add(new_author)
        db.session.commit()
        return response_obj(
            message='Author added successfully',
            data=author_schema.dump(new_author)
        )
    except Exception as e:
        return response_error(
            message='Error while adding author',
            status_code=400
        )


def get_author_by_id(author_id):
    try:
        author = Author.query.get(author_id)
        if author:
            return response_obj(
                message='Author fetched successfully',
                data=author_schema.dump(author)
            )
        return response_error(
            message='Author not found',
            status_code=404
        )
    except Exception as e:
        return response_error(
            message='Error while fetching author',
            status_code=400
        )
