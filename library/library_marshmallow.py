from marshmallow import fields

from .extension import ma


class StudentSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    gender = fields.Str(required=True)
    class_name = fields.Str(required=True)


class CatSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class AuthorSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class BorrowSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    book_id = fields.Int(required=True)
    student_id = fields.Int(required=True)
    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=True)


class BookSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    page_count = fields.Int(required=True)
    author_id = fields.Int(required=True)
    category_id = fields.Int(required=True)

    # class Meta:
    #     fields = ('id', 'name', 'page_count', 'author_id', 'category_id')
