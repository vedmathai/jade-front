class JadeLog:
    def __init__(self):
        self._message = None

    def message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def to_dict(self):
        return {
            'message': self.message(),
        }

    @staticmethod
    def from_dict(val):
        jade_log = JadeLog()
        jade_log.set_message(val['message'])
        return jade_log
