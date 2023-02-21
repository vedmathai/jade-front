import json
from flask import Blueprint, Response, request
from http import HTTPStatus

from jade_front.server.server import Server
from jade_front.services.utils import encode_decode_zip

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/jade-projects/<project_id>/data', methods=['POST'])
def upload_data(project_id):
    server = Server.instance()
    file_string = request.form.get('file')
    zip_file = encode_decode_zip(file_string)
    if file_string is not None:
        server.upload_data(project_id, zip_file)
        response_dict = {"message": "Data uploaded successfully"}
        return Response(
            json.dumps(response_dict),
            HTTPStatus.OK,
            mimetype='application/json',
        )
