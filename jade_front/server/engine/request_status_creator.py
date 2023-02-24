
from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.datamodel.jade_request_status.jade_request_status import JadeRequestStatus


class RequestStatusCreator(AbstractProcessor):
    _instance = None
    _name = 'Requests Status Creator'

    def create(self, logs) -> JadeRequestStatus:
        convert_fns = [
            self.assign_epochs
        ]
        request_status = JadeRequestStatus()
        for fn in convert_fns:
            request_status = fn(logs, request_status)
        return request_status

    def assign_epochs(self, logs, request_status: JadeRequestStatus) -> JadeRequestStatus:
        experiment = logs.experiments()[0]
        current_epoch_i = len(experiment.epochs())
        total_epochs = experiment.total_epochs()
        request_status.set_current_epoch_i(current_epoch_i)
        request_status.set_total_epochs(total_epochs)
        return request_status
