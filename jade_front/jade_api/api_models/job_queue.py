from jade_front.jade_api.api_models.job_queue_item import JobQueueItem


class JobQueue:
    def __init__(self):
        self._job_queue = []

    def job_queue(self):
        return self._job_queue

    def to_dict(self):
        return {
            'job_queue': [i.to_dict() for i in self._job_queue]
        }

    @staticmethod
    def from_ssh_response(rows):
        job_queue = JobQueue()
        for row in rows:
            if len(row) > 0:
                job_queue._job_queue.append(JobQueueItem.from_ssh_response(row))
        job_queue._job_queue.pop(0)
        return job_queue

    @staticmethod
    def from_dict(val):
        job_queue = JobQueue()
        job_queue._job_queue = [JobQueueItem.from_dict(i) for i in val['job_queue']]
        return job_queue
