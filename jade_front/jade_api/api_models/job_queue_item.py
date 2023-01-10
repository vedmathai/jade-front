class JobQueueItem:
    def __init__(self):
        self._job_id = ''
        self._partition = ''
        self._name = ''
        self._user = ''
        self._status = ''
        self._time = ''
        self._nodes = ''
        self._nodelist_reason = ''

    def job_id(self):
        return self._job_id
    
    def partition(self):
        return self._partition

    def name(self):
        return self._name

    def user(self):
        return self._user

    def status(self):
        return self._status

    def time(self):
        return self._time

    def nodes(self):
        return self._nodes

    def nodelist_reason(self):
        return self._nodelist_reason

    def set_job_id(self, job_id):
        self._job_id = job_id
    
    def set_partition(self, partition):
        self._partition = partition

    def set_name(self, name):
        self._name = name

    def set_user(self, user):
        self._user = user

    def set_status(self, status):
        self._status = status

    def set_time(self, time):
        self._time = time

    def set_nodes(self, nodes):
        self._nodes = nodes

    def set_nodelist_reason(self, nodelist_reason):
        self._nodelist_reason = nodelist_reason

    @staticmethod
    def from_ssh_response(item):
        job_queue_item = JobQueueItem()
        item = item.split()
        job_queue_item.set_job_id(item[0])
        job_queue_item.set_partition(item[1])
        job_queue_item.set_name(item[2])
        job_queue_item.set_user(item[3])
        job_queue_item.set_status(item[4])
        job_queue_item.set_time(item[5])
        job_queue_item.set_nodes(item[6])
        job_queue_item.set_nodelist_reason(item[6])
        return job_queue_item

    def to_dict(self):
        return {
            'job_id': self.job_id(),
            'parition': self.partition(),
            'name': self.name(),
            'user': self.user(),
            'status': self.status(),
            'time': self.time(),
            'nodes': self.nodes(),
            'nodelist_reason': self.nodelist_reason(),
        }