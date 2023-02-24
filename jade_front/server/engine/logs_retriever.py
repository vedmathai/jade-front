from jadelogs import JadeLogger
import json
import os
from tempfile import TemporaryDirectory
import zipfile


from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.download_file_api import DownloadFileAPI


class LogsRetriever(AbstractProcessor):
    _instance = None
    _name = 'Logs Retreiver'

    def retrieve_logs(self, project, request):
        download_file_api = DownloadFileAPI()
        temp_folder = TemporaryDirectory()
        remote_filepath = self.remote_log_file_path(project, request)
        local_filepath = os.path.join(temp_folder.name, 'logs.zip')
        download_file_api.download_file(remote_filepath, local_filepath)
        with zipfile.ZipFile(local_filepath, 'r') as zip_ref:
            zip_ref.extractall(temp_folder.name)
        local_log_filepath = os.path.join(temp_folder.name, 'log.json')
        with open(local_log_filepath, 'rt') as f:
            jadelogs = JadeLogger().from_snapshot(json.load(f))
        return jadelogs

    def remote_log_file_path(self, project, request):
        return os.path.join(
            self.remote_log_folder_path(project),
            request.id(),
            self._config.remote_projects_log_file_name(),
        )

    def remote_log_folder_path(self, project):
        return os.path.join(
            self._config.remote_projects_folder_name(),
            project.id(),
            self._config.remote_projects_log_folder_name(),
        )
