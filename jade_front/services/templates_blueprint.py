
from flask import Blueprint, Response
from http import HTTPStatus
import json

from jade_front.server.server import Server

templates_blueprint = Blueprint('request-templates', __name__)

@templates_blueprint.route('/request-templates', methods=['GET'])
def get_templates_list():
    server = Server.instance()
    templates_list = server.get_templates_list()
    return Response(
        json.dumps(templates_list.to_dict()),
        HTTPStatus.OK
    )

@templates_blueprint.route('/request-templates/<template_id>', methods=['GET'])
def get_template(run_id):
    server = Server.instance()
    result = server.get_result(run_id)
    return Response(
        json.dumps({
            'id': '1234',
            'jade_project': '4321',
            'nodes': 1,
            'wallclock_time': '10:00:00',
            'name': '1234',
            'number_gpus': 1,
            'mail_type': 'ALL',
            'mail_user': "john.brown@gmail.com",
            'partition': "small",
            'code_invocation': "PYTHONPATH=. python3 jade-front/8d6b250d-93a8-4924-9f3a-de35c076d320/code/name_classifier/train.py"
        }),
        HTTPStatus.OK
    )
