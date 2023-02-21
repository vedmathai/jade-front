import os

from jade_front.common.config import Config
from jade_front.database.database import Database

class AbstractProcessor:
    def __init__(self):
        self._config = Config.instance()
        self._database = Database.instance()

    _instance = None

    @classmethod
    def instantiate(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.setup()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise Exception('{} not instantiated.'.format(cls._name))
        return cls._instance

    def setup(self):
        pass
