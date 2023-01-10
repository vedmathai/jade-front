from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.list_jobs_api import ListJobsAPI

class JobsLister(AbstractProcessor):
    _instance = None
    _name = 'Jobs Lister'

    def __init__(self):
        super().__init__()
        self.list_jobs_api = ListJobsAPI()

    def list_jobs(self):
        return self.list_jobs_api.run_api()
