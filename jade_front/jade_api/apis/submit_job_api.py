
import os
from tempfile import TemporaryDirectory

from jade_front.jade_api.apis.abstract_api import AbstractAPI
from jade_front.jade_api.apis.unzip_api import UnzipFileAPI


class SubmitJobAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self):
        command = 'sbatch ./src/run_script.sh'
        outputs = super().run_api(command)
        print(outputs)
        for output in outputs:
            job_id = output.strip('Submitted batch job ').strip()
        return job_id
