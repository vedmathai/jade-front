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

    def remote_zip_file_path(self, project):
        return os.path.join(
            self._config.remote_projects_folder_name(),
            project.id(),
            self._config.remote_projects_code_folder_name(),
            self._config.remote_projects_code_file_name(),
        )

    def remote_zip_folder_path(self, project):
        return os.path.join(
            self._config.remote_projects_folder_name(),
            project.id(),
            self._config.remote_projects_code_folder_name(),
        )