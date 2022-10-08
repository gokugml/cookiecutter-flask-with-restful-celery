import os
import sys


def create_empty_app(appname):
    app_files = [
        "__init__.py",
        "models.py",
        "services.py",
        "tasks.py",
    ]
    api_files = [
        "__init__.py",
        "serializers.py",
        "views.py",
    ]

    app_dir = os.path.join(os.path.dirname(__file__), "{{cookiecutter.app_name}}", appname)
    api_dir = os.path.join(app_dir, "api")

    return [os.path.join(app_dir, app) for app in app_files] + [
        os.path.join(api_dir, api) for api in api_files
    ]

def create_test(appname):
    test_dir = os.path.join(
        os.path.dirname(__file__), "tests", "{{cookiecutter.app_name}}", appname
    )
    return [
        os.path.join(test_dir, f)
        for f in ["__init__.py", "api_tests.py", "app_tests.py"]
    ]

def create_app_and_test(appname):
    os.system(f"cp -r {{cookiecutter.app_name}}/{{cookiecutter.sample_app_name}} {{cookiecutter.app_name}}/{appname}")
    os.system(
        f"cp -r tests/{{cookiecutter.app_name}}/{{cookiecutter.sample_app_name}} tests/{{cookiecutter.app_name}}/{appname}"
    )




def os_create(files):
    for f in files:
        dir = os.path.dirname(f)
        if not os.path.isdir(dir):
            os.makedirs(dir)
        open(f, "a").close()


if __name__ == "__main__":
    try:
        app_name = sys.argv[1]
    except IndexError:
        app_name = input("input app name. Please use plural!\t")
    print(app_name)
    create_app_and_test(app_name)
    # files = create_test(app_name)
    # os_create(files)
