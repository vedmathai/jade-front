from jade_front.database.database import Database
from jade_front.server.engine.code_preprocessor import CodePreprocessor
from jade_front.server.engine.data_preprocessor import DataPreprocessor
from jade_front.server.engine.code_runner import CodeRunner
from jade_front.server.engine.logs_retriever import LogsRetriever
from jade_front.server.engine.pollster import Pollster
from jade_front.server.engine.request_status_creator import RequestStatusCreator
from jade_front.server.engine.jobs_lister import JobsLister
from jade_front.server.engine.job_canceller import JobCanceller
from jade_front.datamodel.jade_project.jade_project import JadeProject
from jade_front.datamodel.jade_request.jade_request import JadeRequest


class Server:

    def __init__(self):
        pass

    _instance = None

    @classmethod
    def instantiate(cls, flask_app):
        if cls._instance is None:
            Database.instantiate()
            CodePreprocessor.instantiate()
            DataPreprocessor.instantiate()
            CodeRunner.instantiate()
            LogsRetriever.instantiate()
            Pollster.instantiate()
            RequestStatusCreator.instantiate()
            JobsLister.instantiate()
            JobCanceller.instantiate()
            cls._instance = Server()
            cls._instance.setup()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise Exception('Server not instantiated.')
        return cls._instance

    def setup(self):
        self._code_processor = CodePreprocessor.instance()
        self._data_preprocessor = DataPreprocessor.instance()
        self._code_runner = CodeRunner.instance()
        self._logs_retriever = LogsRetriever.instance()
        self._pollster = Pollster.instance()
        self._request_status_creator = RequestStatusCreator.instance()
        self._jobs_lister = JobsLister.instance()
        self._job_canceller = JobCanceller.instance()
        self._database = Database.instance()
        self._code_processor.setup()
        self._data_preprocessor.setup()
        self._code_runner.setup()
        self._logs_retriever.setup()
        self._pollster.setup()
        self._request_status_creator.setup()
        self._jobs_lister.setup()
        self._jobs_lister.setup()
        self._job_canceller.setup()
        self._database.setup()

    def get_jobs(self):
        jobs = self._jobs_lister.list_jobs()
        return jobs

    def upload_code(self, jade_project_id, code_zip):
        project = self.get_jade_project(jade_project_id)
        self._code_processor.upload_code(project, code_zip)

    def upload_data(self, jade_project_id, data_zip):
        project = self.get_jade_project(jade_project_id)
        self._data_preprocessor.upload_data(project, data_zip)

    def create_request(self, jade_request):
        self._code_runner.run_code(jade_request)
        self._database.write_jade_request(jade_request)

    def get_jade_requests_list(self):
        return self._database.read_jade_requests()

    def get_jade_request(self, jade_request_id):
        return self._database.read_jade_request(jade_request_id)

    def get_new_jade_request(self):
        return JadeRequest.create()

    def delete_jade_request(self, jade_request_id):
        return self._database.delete_jade_request(jade_request_id)

    def cancel_job(self, jade_request_id):
        return self._job_canceller.cancel_job(jade_request_id)

    def create_jade_project(self, jade_project):
        self._database.write_jade_project(jade_project)

    def update_jade_project(self, jade_project):
        self._database.write_jade_project(jade_project)

    def get_jade_projects_list(self):
        return self._database.read_jade_projects()

    def get_new_jade_project(self):
        return JadeProject.create()

    def get_jade_project(self, jade_project_id):
        return self._database.read_jade_project(jade_project_id)

    def delete_jade_project(self, jade_project_id):
        return self._database.delete_jade_project(jade_project_id)

    def get_jade_logs_metadata(self, jade_project_id, jade_request_id):
        jade_project = self.get_jade_project(jade_project_id)
        jade_request = self.get_jade_request(jade_request_id)
        logs = self._logs_retriever.retrieve_logs(jade_project, jade_request)
        return logs

    def get_jade_request_status(self, jade_project_id, jade_request_id):
        logs = self.get_jade_logs_metadata(jade_project_id, jade_request_id)
        request_status = self._request_status_creator.create(logs)
        return request_status
