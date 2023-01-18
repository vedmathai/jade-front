
from jade_front.jade_api.apis.abstract_api import AbstractAPI


class CreateFolderAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self, file_path):
        command = 'mkdir -p {}'.format(file_path)
        outputs = super().run_api(command)
        return outputs
