
from flask import Blueprint, Response
from http import HTTPStatus
import json

from jade_front.server.server import Server

logs_blueprint = Blueprint('logs', __name__)


@logs_blueprint.route('jade-projects/<jade_project_id>/jade-requests/<jade_request_id>/jade-log-metadata', methods=['GET'])
def get_result(jade_project_id, jade_request_id):
    server = Server.instance()
    result = server.get_jade_logs_metadata(jade_project_id, jade_request_id)
    return Response(
        json.dumps(result),
        HTTPStatus.OK
    )
