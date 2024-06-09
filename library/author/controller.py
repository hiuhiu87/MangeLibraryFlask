from flask import Blueprint

from library.author.service import *
from library.constants import API_PREFIX_AUTHOR

author = Blueprint('author', __name__, url_prefix=API_PREFIX_AUTHOR)


@author.route(rule='/', methods=['GET'])
def get_all_authors():
    return get_all()


@author.route(rule='/', methods=['POST'])
def add_author_request():
    return add_author()


@author.route(rule='/<int:author_id>', methods=['GET'])
def get_author_by_id_request(author_id):
    return get_author_by_id(author_id)
