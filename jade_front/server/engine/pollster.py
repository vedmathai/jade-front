from jade_front.server.engine.abstract_processor import AbstractProcessor


class Pollster(AbstractProcessor):
    _instance = None
    _name = 'Pollster'
