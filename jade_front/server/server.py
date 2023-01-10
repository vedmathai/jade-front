from jade_front.server.engine.code_preprocessor import CodePreprocessor
from jade_front.server.engine.code_runner import CodeRunner
from jade_front.server.engine.logs_retriever import LogsRetriever
from jade_front.server.engine.pollster import Pollster
from jade_front.server.engine.results_retriever import ResultsRetriever
from jade_front.server.engine.jobs_lister import JobsLister


class Server:

    def __init__(self):
        pass

    _instance = None

    @classmethod
    def instantiate(cls, flask_app):
        if cls._instance is None:
            CodePreprocessor.instantiate()
            CodeRunner.instantiate()
            LogsRetriever.instantiate()
            Pollster.instantiate()
            ResultsRetriever.instantiate()
            JobsLister.instantiate()
            cls._instance = Server()
            cls._instance.setup()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise Exception('Server not instantiated.')
        return cls._instance

    def setup(self):
        self._code_processor = CodePreprocessor.instance()
        self._code_runner = CodeRunner.instance()
        self._logs_retriever = LogsRetriever.instance()
        self._pollster = Pollster.instance()
        self._results_retriever = ResultsRetriever.instance()
        self._jobs_lister = JobsLister.instance()
        self._code_processor.setup()
        self._code_runner.setup()
        self._logs_retriever.setup()
        self._pollster.setup()
        self._results_retriever.setup()
        self._jobs_lister.setup()

    def get_jobs(self):
        jobs = self._jobs_lister.list_jobs()
        return jobs
