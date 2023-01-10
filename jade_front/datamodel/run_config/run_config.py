class RunConfig:
    def __init__(self):
        self._nodes = None
        self._wallclock_time = None
        self._name = None
        self._number_gpus = None
        self._mail_type = None
        self._mail_user = None

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

    def to_dict(self):
        return {
            'nodes': self.nodes(),
            'wallclock_time': self.wallclock_time(),
            'name': self.name(),
            'number_gpus': self.number_gpus(),
            'mail_type': self.mail_type(),
            'mail_user': self.mail_user(),
        }

    @staticmethod
    def from_dict(val):
        run_config = RunConfig()
        run_config.set_nodes(val['nodes'])
        run_config.set_wallclock_time(val['wallclock_time'])
        run_config.set_name(val['name'])
        run_config.set_number_gpus(val['number_gpus'])
        run_config.set_mail_type(val['mail_type'])
        run_config.set_mail_user(val['mail_user'])
