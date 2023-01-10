from flask import Blueprint, Response
from http import HTTPStatus
import json

from jade_front.server.server import Server

requests_blueprint = Blueprint('requests', __name__)

@requests_blueprint.route('/requests', methods=['GET'])
def get_requests_list():
    server = Server.instance()
    req_data = request.get_json(force=True)
    server.create_organization(req_data)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )

@requests_blueprint.route('/requests/<run_id>', methods=['GET'])
def get_request(run_id):
    server = Server.instance()
    request = server.get_request(run_id)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )

@requests_blueprint.route('/requests', methods=['POST'])
def create_request():
    server = Server.instance()
    request_data = request.get_json()
    server.create_request(request_data)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )
