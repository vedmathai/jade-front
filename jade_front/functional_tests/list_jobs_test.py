import os
from jade_front.datamodel.jade_request.jade_request import JadeRequest
import pytest
import requests
import json


URL = "http://localhost:5000"
version = 'v1'
test_id = '3'
temp_tests_folder = '/tmp/jade_front/tests'


@pytest.mark.skip(reason="Functional Test")
def test_list_processes():
    url = os.path.join(URL, version, 'jobs')
    response = requests.get(url, json={})
    assert len(response.json()) > 0


if __name__ == '__main__':
    test_list_processes()
