

class JadeRequestStatus:
    def __init__(self):
        self._request_id = None
        self._total_epochs = None
        self._current_epoch_i = None
        self._losses = []
        self._train_precision = None
        self._train_recall = None
        self._train_f1 = None
        self._train_exact_match = None
        self._evaluate_precision = None
        self._evaluate_recall = None
        self._evaluate_f1 = None
        self._evaluate_exact_match = None

    def request_id(self):
        return self._request_id

    def total_epochs(self):
        return self._total_epochs

    def current_epoch_i(self):
        return self._current_epoch_i

    def losses(self):
        return self._losses
    
    def train_precision(self):
        return self._train_precision
    
    def train_recall(self):
        return self._train_recall
    
    def train_f1(self):
        return self._train_f1
    
    def train_exact_match(self):
        return self._train_exact_match
    
    def evaluate_precision(self):
        return self._evaluate_precision
    
    def evaluate_recall(self):
        return self._evaluate_recall
    
    def evaluate_f1(self):
        return self._evaluate_f1
    
    def evaluate_exact_match(self):
        return self._evaluate_exact_match
    
    def set_request_id(self, request_id):
        self._request_id = request_id

    def set_total_epochs(self, total_epochs):
        self._total_epochs = total_epochs

    def set_current_epoch_i(self, current_epoch_i):
        self._current_epoch_i = current_epoch_i

    def set_losses(self, losses):
        self._losses = losses

    def set_train_precision(self, train_precision):
        self._train_precision = train_precision
    
    def set_train_recall(self, train_recall):
        self._train_recall = train_recall
    
    def set_train_f1(self, train_f1):
        self._train_f1 = train_f1
    
    def set_train_exact_match(self, train_exact_match):
        self._train_exact_match = train_exact_match

    def set_evaluate_precision(self, evaluate_precision):
        self._evaluate_precision = evaluate_precision
    
    def set_evaluate_recall(self, evaluate_recall):
        self._evaluate_recall = evaluate_recall
    
    def set_evaluate_f1(self, evaluate_f1):
        self._evaluate_f1 = evaluate_f1
    
    def set_evaluate_exact_match(self, evaluate_exact_match):
        self._evaluate_exact_match = evaluate_exact_match

    def to_dict(self):
        return {
            'request_id': self.request_id(),
            'total_epochs': self.total_epochs(),
            'current_epoch_i': self.current_epoch_i(),
            'losses': self.losses(),
            'train_precision': self.train_precision(),
            'train_recall': self.train_recall(),
            'train_f1': self.train_f1(),
            'train_exact_match': self.train_exact_match(),
            'evaluate_precision': self.evaluate_precision(),
            'evaluate_recall': self.evaluate_recall(),
            'evaluate_f1': self.evaluate_f1(),
            'evaluate_exact_match': self.evaluate_exact_match(),
        }

    @staticmethod
    def from_dict(jade_request_dict):
        jade_request_status = JadeRequestStatus()
        jade_request_status.set_request_id(jade_request_dict['id'])
        jade_request_status.set_total_epochs(jade_request_dict['total_epochs'])
        jade_request_status.set_current_epoch_i(jade_request_dict['current_epochs'])
        jade_request_status.set_losses(jade_request_dict['losses'])
        jade_request_status.set_train_precision(jade_request_dict['train_precision'])
        jade_request_status.set_train_recall(jade_request_dict['train_recall'])
        jade_request_status.set_train_f1(jade_request_dict['train_f1'])
        jade_request_status.set_train_exact_match(jade_request_dict['train_precision'])
        jade_request_status.set_evaluate_precision(jade_request_dict['evaluate_precision'])
        jade_request_status.set_evaluate_recall(jade_request_dict['evaluate_recall'])
        jade_request_status.set_evaluate_f1(jade_request_dict['evaluate_f1'])
        jade_request_status.set_evaluate_exact_match(jade_request_dict['evaluate_precision'])
        return jade_request_status
