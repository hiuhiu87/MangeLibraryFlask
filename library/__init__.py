from flask import Flask

from .author.controller import author
from .books.controller import books
from .category.controller import category
from .extension import db, ma


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    from . import models
    with app.app_context():
        db.create_all()
    app.register_blueprint(books)
    app.register_blueprint(author)
    app.register_blueprint(category)
    # print(app.config['SECRET_KEY']) # test loading config
    return app
