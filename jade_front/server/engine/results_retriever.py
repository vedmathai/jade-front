from jade_front.server.engine.abstract_processor import AbstractProcessor


class ResultsRetriever(AbstractProcessor):
    _instance = None
    _name = 'Results Retriever'
