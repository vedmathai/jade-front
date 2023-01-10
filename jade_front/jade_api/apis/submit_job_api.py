
import os
from tempfile import TemporaryDirectory

from jade_front.jade_api.apis.abstract_api import AbstractAPI
from jade_front.jade_api.apis.unzip_api import UnzipAPI


class SubmitJobAPI(AbstractAPI):
    def __init__(self):
        super().__init__()
        self.unzip_api = UnzipAPI

    def run_api(self, run_config):
        self.transfer_code(run_config)
        self.write_script_remote(run_config)
        job_id = self.start_job()
        return job_id

    def create_script(self, run_config):
        script = '#!/bin/bash\n'
        script += '#SBATCH --nodes={}\n'.format(run_config.nodes())
        script += '#SBATCH --time={}\n'.format(run_config.wallclock_time())
        script += '#SBATCH --job-name={}\n'.format(run_config.name())
        script += '#SBATCH --gres=gpu:{}\n'.format(run_config.number_gpus())
        script += '#SBATCH --mail-type={}\n'.format(run_config.mail_type())
        script += '#SBATCH --mail-user={}\n'.format(run_config.mail_user())
        return script

    def transfer_code(self, run_config):
        code_zipfile = run_config.code_zipfile()
        remote_folderpath = run_config.remote_folderpath()
        self.upload_file(code_zipfile, remote_filepath)
        remote_filepath = os.path.join(remote_folderpath, code_zipfile)
        self.unzip_api.run_api(remote_filepath)

    def write_script_remote(self, run_config):
        script_folder = TemporaryDirectory()
        script_file = os.path.join(script_folder.name, 'run_script.sh')
        script_data = self.create_script(run_config)
        with open(script_file, 'wt') as f:
            f.write(script_data)
        self.upload_file(script_file, '.')

    def start_job(self):
        command = 'squeue run_script.sh'
        outputs = super().run_api(command)
        for output in outputs:
            job_id = output
        return job_id