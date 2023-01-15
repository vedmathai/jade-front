from flask import Blueprint, Response, request
from http import HTTPStatus
import json

from jade_front.server.server import Server
from jade_front.datamodel.jade_project.jade_project import JadeProject

projects_blueprint = Blueprint('jade_projects', __name__)

@projects_blueprint.route('/jade_projects', methods=['GET'])
def get_projects_list():
    server = Server.instance()
    jade_projects_list = server.get_jade_projects_list()
    return Response(
        json.dumps(jade_projects_list.to_dict()),
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['GET'])
def get_project(jade_project_id):
    server = Server.instance()
    jade_project = server.get_jade_project(jade_project_id)
    return Response(
        json.dumps(jade_project.to_dict()),
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade_projects', methods=['POST'])
def create_project():
    server = Server.instance()
    request_data = request.json
    jade_project = JadeProject.from_dict(request_data)
    server.create_jade_project(jade_project)
    return Response(
        {'msg': 'Project Created Successfully'},
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['DELETE'])
def delete_project(jade_project_id):
    server = Server.instance()
    server.delete_jade_project(jade_project_id)
    return Response(
        {'msg': 'Jade Project Deleted Successfully'},
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade_projects/<jade_project_id>', methods=['PUT'])
def update_project(jade_project_id):
    server = Server.instance()
    request_data = request.json
    jade_project = JadeProject.from_dict(request_data)
    jade_project.set_id(jade_project_id)
    server.update_jade_project(jade_project)
    return Response(
        {'msg': 'Jade Project Updated Successfully'},
        HTTPStatus.OK
    )