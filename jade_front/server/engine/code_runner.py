import os
from tempfile import TemporaryDirectory


from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.jade_api.apis.upload_file_api import UploadFileAPI
from jade_front.jade_api.apis.unzip_api import UnzipFileAPI
from jade_front.jade_api.apis.submit_job_api import SubmitJobAPI



class CodeRunner(AbstractProcessor):
    _instance = None
    _name = 'Code Runner'

    def run_code(self, jade_request):
        self.write_script_remote(jade_request)
        self.submit_job()

    def create_script(self, jade_request):
        script = '#!/bin/bash\n'
        script += '#SBATCH --nodes={}\n'.format(jade_request.nodes())
        script += '#SBATCH --time={}\n'.format(jade_request.wallclock_time())
        script += '#SBATCH --job-name={}\n'.format(jade_request.name())
        script += '#SBATCH --gres=gpu:{}\n'.format(jade_request.number_gpus())
        script += '#SBATCH --mail-type={}\n'.format(jade_request.mail_type())
        script += '#SBATCH --mail-user={}\n'.format(jade_request.mail_user())
        script += '#SBATCH --partition={}\n'.format(jade_request.partition())
        script += 'python3 ./src/main.py'
        return script

    def write_script_remote(self, jade_request):
        upload_file_api = UploadFileAPI()
        script_folder = TemporaryDirectory()
        script_file = os.path.join(script_folder.name, 'run_script.sh')
        script_data = self.create_script(jade_request)
        with open(script_file, 'wt') as f:
            f.write(script_data)
        upload_file_api.upload_file(script_file, './src/run_script.sh')

    def submit_job(self):
        submit_job_api = SubmitJobAPI()
        job_id = submit_job_api.run_api()
        print(job_id)
