from jade_front.server.engine.abstract_processor import AbstractProcessor


class LogsRetriever(AbstractProcessor):
    _instance = None
    _name = 'Logs Retreiver'
