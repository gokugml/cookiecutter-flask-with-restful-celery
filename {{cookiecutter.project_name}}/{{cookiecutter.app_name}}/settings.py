# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SECRET_KEY = env.str("SECRET_KEY")
SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False


{%- if cookiecutter.use_celery == "yes" %}

REDIS = {
    "host": env.str("REDIS_HOST"),
    "username": env.str("REDIS_USERNAME"),
    "password": env.str("REDIS_PASSWORD"),
}

CELERY = {
    "broker_url": f'redis://{REDIS["username"]}:{REDIS["password"]}@{REDIS["host"]}:6379/0',
    "result_backend": f'redis://{REDIS["username"]}:{REDIS["password"]}@{REDIS["host"]}:6379/1',
}

{%- endif %}


try:
    from {{cookiecutter.app_name}}.local_setting import *
except:
    pass