from flask import Blueprint, Response, request
from http import HTTPStatus
import json
<<<<<<< HEAD
from flask_cors import cross_origin

from jade_front.server.server import Server
from jade_front.datamodel.jade_project.jade_project import JadeProject
HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
    "Access-Control-Allow-Headers":"Origin, X-Requested-With, Content-Type, Accept, Authorization"  # noqa
}

projects_blueprint = Blueprint('jade_projects', __name__)

@projects_blueprint.route('/jade-projects', methods=['GET'])
=======

from jade_front.server.server import Server
from jade_front.datamodel.jade_project.jade_project import JadeProject

projects_blueprint = Blueprint('jade_projects', __name__)

@projects_blueprint.route('/jade_projects', methods=['GET'])
>>>>>>> ca8ba0c2 (CRUD for projects)
def get_projects_list():
    server = Server.instance()
    jade_projects_list = server.get_jade_projects_list()
    return Response(
        json.dumps(jade_projects_list.to_dict()),
        HTTPStatus.OK
    )

<<<<<<< HEAD
@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['GET'])
=======
@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['GET'])
>>>>>>> ca8ba0c2 (CRUD for projects)
def get_project(jade_project_id):
    server = Server.instance()
    jade_project = server.get_jade_project(jade_project_id)
    return Response(
        json.dumps(jade_project.to_dict()),
        HTTPStatus.OK
    )

<<<<<<< HEAD
@projects_blueprint.route('/jade-projects', methods=['POST'])
=======
@projects_blueprint.route('/jade_projects', methods=['POST'])
>>>>>>> ca8ba0c2 (CRUD for projects)
def create_project():
    server = Server.instance()
    request_data = request.json
    jade_project = JadeProject.from_dict(request_data)
    server.create_jade_project(jade_project)
<<<<<<< HEAD
    response =  Response(
        {'msg': 'Project Created Successfully'},
        HTTPStatus.OK,
        headers=HEADERS,
    )
    return response

@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['DELETE'])
=======
    return Response(
        {'msg': 'Project Created Successfully'},
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['DELETE'])
>>>>>>> ca8ba0c2 (CRUD for projects)
def delete_project(jade_project_id):
    server = Server.instance()
    server.delete_jade_project(jade_project_id)
    return Response(
        {'msg': 'Jade Project Deleted Successfully'},
        HTTPStatus.OK
    )

<<<<<<< HEAD
@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['PUT'])
=======
@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['PUT'])
>>>>>>> ca8ba0c2 (CRUD for projects)
def update_project(jade_project_id):
    server = Server.instance()
    request_data = request.json
    jade_project = JadeProject.from_dict(request_data)
    jade_project.set_id(jade_project_id)
    server.update_jade_project(jade_project)
    return Response(
        {'msg': 'Jade Project Updated Successfully'},
        HTTPStatus.OK
<<<<<<< HEAD
    )

@projects_blueprint.route('/jade-projects/new', methods=['GET'])
def new_project():
    server = Server.instance()
    jade_project = server.get_new_jade_project()
    return Response(
        json.dumps(jade_project.to_dict()),
        HTTPStatus.OK
=======
>>>>>>> ca8ba0c2 (CRUD for projects)
    )