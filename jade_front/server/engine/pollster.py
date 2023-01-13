from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.download_file_api import DownloadFileAPI


class Pollster(AbstractProcessor):
    _instance = None
    _name = 'Pollster'

    def poll(self):
        jade_process_status = self.download_file_api