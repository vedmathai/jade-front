import os
from tempfile import TemporaryDirectory


from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.upload_file_api import UploadFileAPI
from jade_front.jade_api.apis.unzip_api import UnzipFileAPI


class CodePreprocessor(AbstractProcessor):
    _instance = None
    _name = 'Code Processor'

    def upload_code(self, code_zip):
        temp_folder = TemporaryDirectory()
        local_filepath = self.store_local(temp_folder, code_zip)
        self.upload_code_helper(local_filepath)
        self.unzip_remote()

    def store_local(self, temp_folder, code_zip):
        tempfile_path = os.path.join(temp_folder.name, 'code.zip')
        with open(tempfile_path, 'wb') as f:
            f.write(code_zip) 
        return tempfile_path

    def upload_code_helper(self, local_filepath):
        upload_file_api = UploadFileAPI()
        upload_file_api.upload_file(local_filepath, './testing123.zip')
    
    def unzip_remote(self):
        unzip_file_api = UnzipFileAPI()
        unzip_file_api.run_api('./testing123.zip')
