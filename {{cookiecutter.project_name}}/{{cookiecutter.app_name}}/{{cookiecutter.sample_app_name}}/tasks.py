from {{cookiecutter.app_name}}.extensions import celery


@celery.task
def dummy_task():
    print("celery dummy_task ok")
    return "OK"
