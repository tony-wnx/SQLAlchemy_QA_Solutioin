# #-*-coding:utf-8-*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config

# #初始化数据库对象
db = SQLAlchemy()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    config_name = os.getenv('APP_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .view import bp
    app.register_blueprint(bp)

    return app
