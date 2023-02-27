

class JadeRequestStatus:
    def __init__(self):
        self._request_id = None
        self._total_epochs = None
        self._current_epoch_i = None
        self._losses = []

    def request_id(self):
        return self._request_id

    def total_epochs(self):
        return self._total_epochs

    def current_epoch_i(self):
        return self._current_epoch_i

    def losses(self):
        return self._losses

    def set_request_id(self, request_id):
        self._request_id = request_id

    def set_total_epochs(self, total_epochs):
        self._total_epochs = total_epochs

    def set_current_epoch_i(self, current_epoch_i):
        self._current_epoch_i = current_epoch_i

    def set_losses(self, losses):
        self._losses = losses

    def to_dict(self):
        return {
            'request_id': self.request_id(),
            'total_epochs': self.total_epochs(),
            'current_epoch_i': self.current_epoch_i(),
            'losses': self.losses(),
        }

    @staticmethod
    def from_dict(jade_request_dict):
        jade_request_status = JadeRequestStatus()
        jade_request_status.set_request_id(jade_request_dict['id'])
        jade_request_status.set_total_epochs(jade_request_dict['total_epochs'])
        jade_request_status.set_current_epoch_i(jade_request_dict['current_epochs'])
        jade_request_status.set_losses(jade_request_dict['losses'])
        return jade_request_status
