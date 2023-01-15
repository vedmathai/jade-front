import os
import pytest
import requests
import json
import uuid

from jade_front.jade_api.api_models.job_queue import JobQueue
from jade_front.datamodel.jade_project.jade_project_list import JadeProjectList
from jade_front.datamodel.jade_project.jade_project import JadeProject



URL = "http://localhost:5000"
version = 'v1'
test_id = '3'
temp_tests_folder = '/tmp/jade_front/tests'
code_location = 'jade_front/functional_tests/test_code.zip'

@pytest.mark.skip(reason="Functional Test")
def crud_projects_test():
    project = create_project()
    project = update_project(project)
    delete_project(project)

def create_project():
    # Create project
    url = os.path.join(URL, version, 'jade_projects','new')
    project_dict = requests.get(url).json()
    project = JadeProject.from_dict(project_dict)
    project.set_name('test')
    url = os.path.join(URL, version, 'jade_projects')
    requests.post(url, json=project.to_dict())

    # Check project list greater than 1
    url = os.path.join(URL, version, 'jade_projects')
    response = requests.get(url)
    projects = JadeProjectList.from_dict(response.json())
    assert len(projects.jade_project_list()) > 1

    # Retrieve project by ID
    first = projects.jade_project_list()[0]
    url = os.path.join(URL, version, 'jade_projects', first.id())
    response = requests.get(url)
    project = JadeProject.from_dict(response.json())
    assert projects.jade_project_list()[0].to_dict() == project.to_dict()
    return project

def update_project(project):
    project.set_name('test_test')
    url = os.path.join(URL, version, 'jade_projects', project.id())
    new_project = JadeProject.from_dict(project.to_dict())
    new_project.set_id(str(uuid.uuid4()))  # Check if change of ID is ignored on server
    requests.put(url, json=new_project.to_dict())
    response = requests.get(url)
    new_project = JadeProject.from_dict(response.json())
    assert new_project.to_dict() == project.to_dict()
    return new_project

def delete_project(project):
    # Check project is in list of projects
    url = os.path.join(URL, version, 'jade_projects')
    response = requests.get(url)
    projects = JadeProjectList.from_dict(response.json())
    assert project.id() in [i.id() for i in projects.jade_project_list()]

    # Delete Project
    url = os.path.join(URL, version, 'jade_projects', project.id())
    requests.delete(url)

    # Check that the project is now not there in the list of projects
    url = os.path.join(URL, version, 'jade_projects')
    response = requests.get(url)
    projects = JadeProjectList.from_dict(response.json())
    assert project.id() not in [i.id() for i in projects.jade_project_list()]


if __name__ == '__main__':
    crud_projects_test()
