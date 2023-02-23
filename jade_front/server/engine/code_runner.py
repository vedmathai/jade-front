import os
import re
from tempfile import TemporaryDirectory


from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.upload_file_api import UploadFileAPI
from jade_front.jade_api.apis.submit_job_api import SubmitJobAPI



class CodeRunner(AbstractProcessor):
    _instance = None
    _name = 'Code Runner'

    def run_code(self, jade_request):
        self.write_script_remote(jade_request)
        job_id = self.submit_job(jade_request)
        self.save_jade_request(job_id, jade_request)

    def create_script(self, jade_request):
        script_lines = [
            '#!/bin/bash\n',
            '#SBATCH --nodes={}\n'.format(jade_request.nodes()),
            '#SBATCH --time={}\n'.format(jade_request.wallclock_time()),
            '#SBATCH --job-name={}\n'.format(jade_request.name()),
            '#SBATCH --gres=gpu:{}\n'.format(jade_request.number_gpus()),
            '#SBATCH --mail-type={}\n'.format(jade_request.mail_type()),
            '#SBATCH --mail-user={}\n'.format(jade_request.mail_user()),
            '#SBATCH --partition={}\n'.format(jade_request.partition()),
            self.venv_invocation(jade_request),
            self.code_invocation(jade_request),
        ]
        script = ''
        for line in script_lines:
            script += '{}\n'.format(line)
        return script

    def write_script_remote(self, jade_request):
        upload_file_api = UploadFileAPI()
        script_folder = TemporaryDirectory()
        script_file = os.path.join(script_folder.name, 'run_script.sh')
        script_data = self.create_script(jade_request)
        with open(script_file, 'wt') as f:
            f.write(script_data)
        remote_run_script_file = self.remote_run_script_file(jade_request)
        upload_file_api.upload_file(script_file, remote_run_script_file)

    def submit_job(self, jade_request):
        submit_job_api = SubmitJobAPI()
        remote_run_script_file = self.remote_run_script_file(jade_request)
        job_id = submit_job_api.run_api(remote_run_script_file)
        return job_id

    def save_jade_request(self, job_id, jade_request):
        jade_request.set_job_id(job_id)
        self._database.write_jade_request(jade_request)

    def venv_invocation(self, jade_request):
        venv_location = os.path.join(
            self._config.remote_projects_folder_name(),
            jade_request.jade_project(),
            'venv/bin/activate'
        )
        venv_invocation = "source {}".format(venv_location)
        return venv_invocation

    def code_invocation(self, jade_request):
        project = self._database.read_jade_project(jade_request.jade_project())
        folder_path = self.remote_zip_folder_path(project)
        code_invocation = jade_request.code_invocation()
        project_id_env_assignment = 'PROJECT_ID={}'.format(jade_request.jade_project())
        request_id_env_assignment = 'REQUEST_ID={}'.format(jade_request.id())
        code_invocation = re.sub(
            'REMOTE_CODE_FOLDER_PATH',
            folder_path,
            code_invocation
        )
        code_invocation = [
            project_id_env_assignment,
            request_id_env_assignment,
            code_invocation
        ]
        code_invocation = ' '.join(code_invocation)
        return code_invocation

    def remote_run_script_file(self, jade_request):
        project = self._database.read_jade_project(jade_request.jade_project())
        remote_run_script_folder = self.remote_zip_folder_path(project)
        remote_run_script_file = '{}/run_script.sh'.format(remote_run_script_folder)
        return remote_run_script_file

    def remote_zip_file_path(self, project):
        return os.path.join(
            self.remote_zip_folder_path(project),
            self._config.remote_projects_code_file_name(),
        )

    def remote_zip_folder_path(self, project):
        return os.path.join(
            self._config.remote_projects_folder_name(),
            project.id(),
            self._config.remote_projects_code_folder_name(),
        )
