from flask import request

from library.library_marshmallow import CatSchema
from library.models import Category
from library.utils import response_obj, response_error
from ..extension import db

category_schema = CatSchema()
categorys_schema = CatSchema(many=True)


def get_all_cate():
    try:
        categorys = Category.query.all()
        return response_obj(
            message='Category fetched successfully',
            data=categorys_schema.dump(categorys)
        )
    except Exception as e:
        return response_error(
            message='Error while fetching categorys',
            status_code=400
        )


def add_cate():
    try:
        data = request.get_json()
        result = category_schema.load(data)
        new_category = Category(
            name=result['name']
        )
        db.session.add(new_category)
        db.session.commit()
        return response_obj(
            message='Category added successfully',
            data=category_schema.dump(new_category)
        )
    except Exception as e:
        return response_error(
            message='Error while adding category',
            status_code=400
        )


def get_cate_by_id(id):
    try:
        category = Category.query.get(id)
        return response_obj(
            message='Category fetched successfully',
            data=category_schema.dump(category)
        )
    except Exception as e:
        return response_error(
            message='Error while fetching category',
            status_code=400
        )
