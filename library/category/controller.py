from flask import Blueprint

from .service import *
from ..constants import API_PREFIX_CATEGORY

category = Blueprint('category', __name__, url_prefix=API_PREFIX_CATEGORY)


@category.route(rule='/', methods=['GET'])
def get_all_cate_request():
    return get_all_cate()


@category.route(rule='/', methods=['POST'])
def add_cate_request():
    return add_cate()


@category.route(rule='/<int:id>', methods=['GET'])
def get_cate_by_id_request(id):
    return get_cate_by_id(id)
