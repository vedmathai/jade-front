import json
from flask import Blueprint, Response
from http import HTTPStatus

from jade_front.server.server import Server

jobs_blueprint = Blueprint('jobs', __name__)

@jobs_blueprint.route('/jobs', methods=['GET'])
def get_jobs_list():
    server = Server.instance()
    jobs = server.get_jobs()
    return Response(
        json.dumps(jobs.to_dict()),
        HTTPStatus.OK
    )
