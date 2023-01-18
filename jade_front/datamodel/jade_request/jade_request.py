import uuid


class JadeRequest:
    def __init__(self):
        self._id = None
        self._jade_project = None
        self._nodes = None
        self._wallclock_time = None
        self._name = None
        self._number_gpus = None
        self._mail_type = None
        self._mail_user = None
        self._partition = None
        self._job_id = None
        self._code_invocation = None

    def id(self):
        return self._id

    def jade_project(self):
        return self._jade_project

    def nodes(self):
        return self._nodes

    def wallclock_time(self):
        return self._wallclock_time

    def name(self):
        return self._name

    def number_gpus(self):
        return self._number_gpus

    def mail_type(self):
        return self._mail_type

    def mail_user(self):
        return self._mail_user

    def partition(self):
        return self._partition

    def job_id(self):
        return self._job_id

    def code_invocation(self):
        return self._code_invocation

    def set_id(self, id):
        self._id = id

    def set_jade_project(self, jade_project):
        self._jade_project = jade_project

    def set_nodes(self, nodes):
        self._nodes = nodes

    def set_wallclock_time(self, wallclock_time):
        self._wallclock_time = wallclock_time

    def set_name(self, name):
        self._name = name

    def set_number_gpus(self, number_gpus):
        self._number_gpus = number_gpus

    def set_mail_type(self, mail_type):
        self._mail_type = mail_type

    def set_mail_user(self, mail_user):
        self._mail_user = mail_user
    
    def set_parition(self, partition):
        self._partition = partition

    def set_job_id(self, job_id):
        self._job_id = job_id

    def set_code_invocation(self, code_invocation):
        self._code_invocation = code_invocation

    def to_dict(self):
        return {
            'id': self.id(),
            'jade_project': self.jade_project(),
            'nodes': self.nodes(),
            'wallclock_time': self.wallclock_time(),
            'name': self.name(),
            'number_gpus': self.number_gpus(),
            'mail_type': self.mail_type(),
            'mail_user': self.mail_user(),
            'partition': self.partition(),
            'job_id': self.job_id(),
            'code_invocation': self.code_invocation()
        }

    @staticmethod
    def from_dict(jade_request_dict):
        jade_request = JadeRequest()
        jade_request.set_id(jade_request_dict['id'])
        jade_request.set_jade_project(jade_request_dict['jade_project'])
        jade_request.set_nodes(jade_request_dict['nodes'])
        jade_request.set_wallclock_time(jade_request_dict['wallclock_time'])
        jade_request.set_name(jade_request_dict['name'])
        jade_request.set_number_gpus(jade_request_dict['number_gpus'])
        jade_request.set_mail_type(jade_request_dict['mail_type'])
        jade_request.set_mail_user(jade_request_dict['mail_user'])
        jade_request.set_parition(jade_request_dict['partition'])
        jade_request.set_job_id(jade_request_dict['job_id'])
        jade_request.set_code_invocation(jade_request_dict['code_invocation'])
        return jade_request

    @staticmethod
    def create():
        jade_request = JadeRequest()
        jade_request.set_id(str(uuid.uuid4()))
        return jade_request
