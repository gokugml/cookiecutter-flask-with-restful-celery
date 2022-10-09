# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
{%- if cookiecutter.use_celery == "yes" %}
from celery import Celery
{%- endif %}
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf.csrf import CSRFProtect

from {{cookiecutter.app_name}}.utils.apispec import APISpecExt

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
{%- if cookiecutter.use_celery == "yes" %}
celery = Celery()
{%- endif %}
apispec = APISpecExt()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
