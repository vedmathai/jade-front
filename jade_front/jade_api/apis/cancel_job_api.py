
from jade_front.jade_api.apis.abstract_api import AbstractAPI


class CancelJobAPI(AbstractAPI):
    def __init__(self):
        super().__init__()

    def run_api(self, jade_request):
        command = 'scancel {}'.format(jade_request.job_id())
        super().run_api(command)
        return
