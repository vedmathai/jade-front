from flask import Blueprint, Response, request
from http import HTTPStatus
import json

from jade_front.server.server import Server
from jade_front.datamodel.jade_request.jade_request import JadeRequest

requests_blueprint = Blueprint('jade_requests', __name__)

@requests_blueprint.route('/jade_requests', methods=['GET'])
def get_requests_list():
    server = Server.instance()
    jade_requests_list = server.get_jade_requests_list()
    return Response(
        json.dumps([i.to_dict() for i in jade_requests_list]),
        HTTPStatus.OK
    )

@requests_blueprint.route('/jade_requests/<jade_request_id>', methods=['GET'])
def get_request(jade_request_id):
    server = Server.instance()
    jade_request = server.get_jade_request(jade_request_id)
    return Response(
        json.dumps(jade_request.to_dict()),
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

@requests_blueprint.route('/jade_requests/<jade_request_id>', methods=['DELETE'])
def delete_request(jade_request_id):
    server = Server.instance()
    server.delete_jade_request(jade_request_id)
    return Response(
        {'msg': 'Jade Request Deleted Successfully'},
        HTTPStatus.OK
    )

@requests_blueprint.route('/jade_requests/<jade_request_id>/cancel', methods=['POST'])
def cancel_jade_request(jade_request_id):
    server = Server.instance()
    server.cancel_job(jade_request_id)
    return Response(
        {'msg': 'Jade Request Cancelled Successfully'},
        HTTPStatus.OK
    )