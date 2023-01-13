import os
from jade_front.datamodel.jade_request.jade_request import JadeRequest
import pytest
import requests
import json
import uuid


URL = "http://localhost:5000"
version = 'v1'
test_id = '3'
temp_tests_folder = '/tmp/jade_front/tests'
code_location = 'jade_front/functional_tests/test_code.zip'

@pytest.mark.skip(reason="Functional Test")
def upload_run_test():
    #upload_code()
    start_processing()

def upload_code():
    with open(code_location, 'rb') as f:
        data = f.read()
        url = os.path.join(URL, version, 'code')
        requests.post(url, data=data)

def start_processing():
    request = create_request()
    url = os.path.join(URL, version, 'jade_requests')
    requests.post(url, json=request.to_dict())

def create_request():
    request = JadeRequest()
    request.set_id(str(uuid.uuid4()))
    request.set_nodes('1')
    request.set_wallclock_time('10:00:00')
    request.set_name('job123')
    request.set_number_gpus('1')
    request.set_mail_type('ALL')
    request.set_mail_user('john.brown@gmail.com')
    request.set_parition('small')
    return request


if __name__ == '__main__':
    upload_run_test()
