import json
import os
from tempfile import TemporaryDirectory

from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.download_file_api import DownloadFileAPI
from jade_front.datamodel.jade_log.jade_log import JadeLog

class LogsRetriever(AbstractProcessor):
    _instance = None
    _name = 'Logs Retriever'

    def retrieve_logs(self, jade_request_id):
        temp_dir = TemporaryDirectory()
        local_filepath = os.path.join(temp_dir.name, 'log.json')
        download_file_api = DownloadFileAPI()
        remote_filepath = './log.json'
        download_file_api.download_file(remote_filepath, local_filepath)
        with open(local_filepath, 'rt') as f:
            logs_dict = json.load(f)
            logs = JadeLog.from_dict(logs_dict)
        return logs_dict
