import json
from flask import Blueprint, Response, request
from http import HTTPStatus

from jade_front.server.server import Server
from jade_front.services.utils import encode_decode_zip

code_blueprint = Blueprint('code', __name__)

@code_blueprint.route('/projects/<project_id>/code', methods=['POST'])
def upload_code(project_id):
    server = Server.instance()
    file_string = request.form.get('file')
    zip_file = encode_decode_zip(file_string)
    if file_string is not None:
        server.upload_code(zip_file)
        response_dict = {"message": "Bulk reports uploaded successfully"}
        return Response(
            json.dumps(response_dict),
            HTTPStatus.OK,
            mimetype='application/json',
        )
