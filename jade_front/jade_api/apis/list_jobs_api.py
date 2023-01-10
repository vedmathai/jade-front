
from jade_front.jade_api.apis.abstract_api import AbstractAPI
from jade_front.jade_api.api_models.job_queue import JobQueue


class ListJobsAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self):
        command = 'squeue'
        outputs = super().run_api(command)
        buffer = ''
        rows = []
        for output in outputs:
            for char in output:
                if char == '\n':
                    rows.append(buffer)
                    buffer = ''
                else:
                    buffer += char
        rows.append(buffer)
        job_queue = JobQueue.from_ssh_response(rows)
        return job_queue
