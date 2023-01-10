
from flask import Blueprint, Response
from http import HTTPStatus
import json

from jade_front.server.server import Server

results_blueprint = Blueprint('results', __name__)

@results_blueprint.route('/results', methods=['GET'])
def get_result_list():
    server = Server.instance()
    results_list = server.get_results_list()
    return Response(
        json.dumps(results_list.to_dict()),
        HTTPStatus.OK
    )

@results_blueprint.route('/results/<run_id>', methods=['GET'])
def get_result(run_id):
    server = Server.instance()
    result = server.get_result(run_id)
    return Response(
        json.dumps(result),
        HTTPStatus.OK
    )