import json
from flask import Blueprint, Response, request
from http import HTTPStatus

from jade_front.server.server import Server

code_blueprint = Blueprint('code', __name__)

@code_blueprint.route('/code', methods=['POST'])
def upload_code():
    server = Server.instance()
    code_data = request.data
    server.upload_code(code_data)
    return Response(
        {'message': 'Code has been uploaded successfully.'},
        HTTPStatus.OK
    )
