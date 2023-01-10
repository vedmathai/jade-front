from jade_front.server.engine.abstract_processor import AbstractProcessor


class CodeRunner(AbstractProcessor):
    _instance = None
    _name = 'Code Runner'
