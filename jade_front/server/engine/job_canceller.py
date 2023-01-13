
from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.cancel_job_api import CancelJobAPI
from jade_front.database.database import Database



class JobCanceller(AbstractProcessor):
    _instance = None
    _name = 'Job Canceller'

    def cancel_job(self, jade_request_id):
        database = Database.instance()
        cancel_job_api = CancelJobAPI()
        jade_request = database.read_jade_request(jade_request_id)
        cancel_job_api.run_api(jade_request)
