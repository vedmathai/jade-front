
from tempfile import TemporaryDirectory

from jade_front.jade_api.apis.abstract_api import AbstractAPI


class SubmitJobAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self, remote_run_script_file):
        command = 'sbatch {}'.format(remote_run_script_file)
        outputs = super().run_api(command)
        for output in outputs:
            job_id = output.strip('Submitted batch job ').strip()
        return job_id
