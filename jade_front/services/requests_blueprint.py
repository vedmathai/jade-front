from flask import Blueprint, Response, request
from http import HTTPStatus
import json

from jade_front.server.server import Server
from jade_front.datamodel.jade_request.jade_request import JadeRequest

requests_blueprint = Blueprint('jade_requests', __name__)

@requests_blueprint.route('/jade_requests', methods=['GET'])
def get_requests_list():
    server = Server.instance()
    req_data = request.get_json(force=True)
    server.create_organization(req_data)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )

@requests_blueprint.route('/jade_requests/<run_id>', methods=['GET'])
def get_request(run_id):
    server = Server.instance()
    request = server.get_request(run_id)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )

@requests_blueprint.route('/jade_requests', methods=['POST'])
def create_request():
    server = Server.instance()
    request_data = request.json
    jade_request = JadeRequest.from_dict(request_data)
    server.create_request(jade_request)
    return Response(
        {'msg': 'Request Created Successfully'},
        HTTPStatus.OK
    )
