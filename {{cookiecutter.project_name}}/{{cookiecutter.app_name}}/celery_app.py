from {{cookiecutter.app_name}}.app import register_celery

app = register_celery()
app.conf.imports = app.conf.imports + ("{{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.tasks",)
