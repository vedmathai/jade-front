import os
import pytest
import requests
import json
import uuid

from jade_front.jade_api.api_models.job_queue import JobQueue
from jade_front.datamodel.jade_request.jade_request import JadeRequest


URL = "http://localhost:5000"
version = 'v1'
test_id = '3'
temp_tests_folder = '/tmp/jade_front/tests'
code_location = 'jade_front/functional_tests/test_code.zip'

@pytest.mark.skip(reason="Functional Test")
def upload_run_test():
    upload_code()
    start_processing()
    get_requests()
    get_request()
    cancel_request()
    delete_request()

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

def get_requests():
    url = os.path.join(URL, version, 'jade_requests')
    response = requests.get(url)
    jade_requests = [JadeRequest.from_dict(i) for i in response.json()]
    assert all(int(i.job_id()) > 400000 for i in jade_requests)

def get_request():
    url = os.path.join(URL, version, 'jade_requests')
    response = requests.get(url)
    jade_requests = [JadeRequest.from_dict(i) for i in response.json()]
    first = jade_requests[0]
    url = os.path.join(URL, version, 'jade_requests', first.id())
    response = requests.get(url)
    jade_request = JadeRequest.from_dict(response.json())
    assert jade_request.to_dict() == first.to_dict()

def delete_request():
    jade_requests_url = os.path.join(URL, version, 'jade_requests')
    response = requests.get(jade_requests_url)
    jade_requests = [JadeRequest.from_dict(i) for i in response.json()]
    first = jade_requests[0]
    delete_url = os.path.join(URL, version, 'jade_requests', first.id())
    requests.delete(delete_url)
    response = requests.get(jade_requests_url)
    jade_requests = [JadeRequest.from_dict(i) for i in response.json()]
    jade_requests_ids = [i.id() for i in jade_requests]
    assert first.id() not in jade_requests_ids

def cancel_request():
    jade_requests_url = os.path.join(URL, version, 'jade_requests')
    response = requests.get(jade_requests_url)
    jade_requests = [JadeRequest.from_dict(i) for i in response.json()]
    first = jade_requests[0]
    job_queue = get_job_queue()
    job_queue_ids = [job.job_id() for job in job_queue.job_queue()]
    assert first.job_id() in job_queue_ids
    cancel_url = os.path.join(URL, version, 'jade_requests', first.id(), 'cancel')
    requests.post(cancel_url)
    job_queue = get_job_queue()
    job_queue_ids = [job.job_id() for job in job_queue.job_queue()]
    assert first.job_id() not in job_queue_ids

def get_job_queue():
    url = os.path.join(URL, version, 'jobs')
    response = requests.get(url).json()
    job_queue = JobQueue.from_dict(response)
    return job_queue


if __name__ == '__main__':
    upload_run_test()
