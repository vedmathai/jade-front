from jade_front.server.engine.abstract_processor import AbstractProcessor


class CodePreprocessor(AbstractProcessor):
    _instance = None
    _name = 'Code Processor'
