from flask import Blueprint, Response, request
from http import HTTPStatus
import json
from flask_cors import cross_origin

from jade_front.server.server import Server
from jade_front.datamodel.jade_project.jade_project import JadeProject
from jade_front.services.utils import encode_decode_zip


HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
    "Access-Control-Allow-Headers":"Origin, X-Requested-With, Content-Type, Accept, Authorization"  # noqa
}

projects_blueprint = Blueprint('jade_projects', __name__)

@projects_blueprint.route('/jade-projects', methods=['GET'])
def get_projects_list():
    server = Server.instance()
    jade_projects_list = server.get_jade_projects_list()
    return Response(
        json.dumps(jade_projects_list.to_dict()),
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['GET'])
def get_project(jade_project_id):
    server = Server.instance()
    print(jade_project_id)
    jade_project = server.get_jade_project(jade_project_id)
    return Response(
        json.dumps(jade_project.to_dict()),
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade-projects', methods=['POST'])
def create_project():
    server = Server.instance()
    request_data = request.json
    jade_project = JadeProject.from_dict(request_data)
    server.create_jade_project(jade_project)
    response =  Response(
        {'msg': 'Project Created Successfully'},
        HTTPStatus.OK,
        headers=HEADERS,
    )
    return response

@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['DELETE'])
def delete_project(jade_project_id):
    server = Server.instance()
    server.delete_jade_project(jade_project_id)
    return Response(
        {'msg': 'Jade Project Deleted Successfully'},
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade-projects/<jade_project_id>', methods=['PUT'])
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

@projects_blueprint.route('/jade-projects/new', methods=['GET'])
def new_project():
    server = Server.instance()
    jade_project = server.get_new_jade_project()
    return Response(
        json.dumps(jade_project.to_dict()),
        HTTPStatus.OK
    )

@projects_blueprint.route('/jade-projects/<project_id>/code', methods=['POST'])
def upload_code(project_id):
    server = Server.instance()
    file_string = request.form.get('file')
    zip_file = encode_decode_zip(file_string)
    if file_string is not None:
        server.upload_code(project_id, zip_file)
        response_dict = {"message": "Bulk reports uploaded successfully"}
        return Response(
            json.dumps(response_dict),
            HTTPStatus.OK,
            mimetype='application/json',
            headers=HEADERS,
        )
