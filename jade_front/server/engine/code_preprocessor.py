import os
from tempfile import TemporaryDirectory


from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.upload_file_api import UploadFileAPI
from jade_front.jade_api.apis.create_folder_api import CreateFolderAPI
from jade_front.jade_api.apis.unzip_api import UnzipFileAPI

LOCAL_PROJECT_CODE_NAME = "code.zip"

class CodePreprocessor(AbstractProcessor):
    _instance = None
    _name = 'Code Processor'

    def upload_code(self, project, code_zip):
        temp_folder = TemporaryDirectory()
        local_filepath = self.store_local(temp_folder, code_zip)
        self.create_remote_folder_helper(project)
        self.upload_code_helper(local_filepath, project)
        self.unzip_remote(project)

    def store_local(self, temp_folder, code_zip):
        tempfile_path = os.path.join(temp_folder.name, LOCAL_PROJECT_CODE_NAME)
        with open(tempfile_path, 'wb') as f:
            f.write(code_zip) 
        return tempfile_path

    def upload_code_helper(self, local_filepath, project):
        upload_file_api = UploadFileAPI()
        remote_zip_file_path = self.remote_zip_file_path(project)
        upload_file_api.upload_file(local_filepath, remote_zip_file_path)

    def create_remote_folder_helper(self, project):
        create_folder = CreateFolderAPI()
        remote_zip_folder_path = self.remote_zip_folder_path(project)
        create_folder.run_api(remote_zip_folder_path)
    
    def unzip_remote(self, project):
        unzip_file_api = UnzipFileAPI()
        remote_zip_file_path = self.remote_zip_file_path(project)
        remote_zip_folder_path = self.remote_zip_folder_path(project)
        unzip_file_api.run_api(remote_zip_file_path, remote_zip_folder_path)
