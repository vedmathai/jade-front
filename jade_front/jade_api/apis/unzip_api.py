
import os
from tempfile import TemporaryDirectory

from jade_front.jade_api.apis.abstract_api import AbstractAPI


class UnzipAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self, file_path):
        command = 'unzip {}'.format(file_path)
        outputs = super().run_api(command)
        return outputs[0]
