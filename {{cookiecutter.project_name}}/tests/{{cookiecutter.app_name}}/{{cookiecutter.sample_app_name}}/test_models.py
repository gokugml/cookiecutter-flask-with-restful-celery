import pytest

from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.models import Sample


@pytest.mark.skip("smaple test")
@pytest.mark.usefixtures("db")
class TestSample:

    # @pytest.mark.parametrize()
    def test_sample(self):
        samples = [
            ("sample1", "email-1"),
            ("sample1", "email-2"),
            ("sample2", "email-2"),
            ("sample2", "email-2"),
        ]
        for s in samples:
            sample = Sample(name=s[0], email=s[1])
            sample.save()

        queryed = Sample.query.filter_by(name="sample1")
        assert queryed.first().id == 1
        objects = Sample.get_by_id(2)
        assert (objects.name, objects.email) == ("sample1", "email-2")

        queryed = Sample.query.filter_by(email="email-2")
        assert queryed[1].name == queryed[2].name
        assert queryed.paginate().total == 3
