
from jade_front.jade_api.apis.abstract_api import AbstractAPI


class UnzipFileAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self, src_file_path, dest_file_path=None):
        command = 'unzip -o {}'.format(src_file_path)
        if dest_file_path is not None:
            command = 'unzip -o {} -d {}'.format(src_file_path, dest_file_path)
        outputs = super().run_api(command)
        return outputs[0]
