"""Post gen hook to ensure that the generated project
has only one package management, either pipenv or pip."""
import logging
import os
import shutil
import sys

_logger = logging.getLogger()


def clean_extra_package_management_files():
    """Removes either requirements files and folder or the Pipfile."""
    use_pipenv = "{{cookiecutter.use_pipenv}}"
    use_heroku = "{{cookiecutter.use_heroku}}"
    use_github = "{{cookiecutter.github_username}}"
    use_celery = "{{cookiecutter.use_celery}}"
    custom_pipconf = "{{cookiecutter.custom_pipconf}}"
    to_delete = []

    if use_pipenv == "True":
        to_delete = to_delete + ["requirements.txt", "requirements"]
    else:
        to_delete.append("Pipfile")

    if use_heroku == "False":
        to_delete = to_delete + ["Procfile", "app.json"]

    if use_github == "":
        to_delete = to_delete + [".github"]

    if use_celery == "no":
        base_path = os.getcwd()
        app_path = os.path.join(
            base_path,
            '{{cookiecutter.app_name}}'
        )
        tasks_path = os.path.join(app_path, '{{cookiecutter.sample_app_name}}', 'tasks.py')
        celery_app_path = os.path.join(app_path, 'celery_app.py')
        to_delete = to_delete + [tasks_path, celery_app_path]
    if custom_pipconf == "no":
        to_delete = to_delete + ["pip.conf"]
        
    try:
        for file_or_dir in to_delete:
            if os.path.isfile(file_or_dir):
                os.remove(file_or_dir)
            else:
                shutil.rmtree(file_or_dir)
        shutil.copy(".env.example", ".env")
    except OSError as e:
        _logger.warning("While attempting to remove file(s) an error occurred")
        _logger.warning(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    clean_extra_package_management_files()
