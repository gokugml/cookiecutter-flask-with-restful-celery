import pytest
from flask import url_for

from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.models import Sample


@pytest.mark.skip("smaple test")
@pytest.mark.usefixtures("db")
class TestSampleApi:
    def test_get(self, client):
        # test 404
        sample_url = url_for("api.sample", id=1)
        rep = client.get(sample_url)
        assert rep.status_code == 404

        samples = [
            ("sample1", "email-1"),
            ("sample1", "email-2"),
            ("sample2", "email-2"),
            ("sample2", "email-2"),
        ]
        for s in samples:
            sample = Sample(name=s[0], email=s[1])
            sample.save()

        sample_url = url_for("api.sample", id=1)
        rep = client.get(sample_url)
        data = rep.get_json()["data"]
        assert (data["name"], data["email"]) == samples[0]

        sample_url = url_for("api.samplelist")
        print(f"api.samplelist {sample_url}")
        rep = client.get(sample_url)
        assert rep.status_code == 200
        assert rep.get_json()["data"]["total"] == 4
