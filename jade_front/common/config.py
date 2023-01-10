import json


config_files = {
    'local': 'jade_front/common/configs/local_config.json',
}

class Config:
    _instance = None

    def __init__(self):
        self._keyring_file = None
        self._private_key_file = None
        self._jade_hostname = None
        self._jade_username = None

    @staticmethod
    def instantiate(tier) -> None:
        config_file = config_files.get(tier)
        with open(config_file, 'rt') as f:
            config = Config.from_dict(json.load(f))
        Config._instance = config

    @staticmethod
    def instance() -> "Config":
        if Config._instance is None:
            raise Exception('Config not instantiated, use Config.instantiate() function first')  # noqa
        return Config._instance

    def keyring_file(self) -> str:
        return self._keyring_file

    def private_key_file(self) -> str:
        return self._private_key_file

    def jade_hostname(self) -> str:
        return self._jade_hostname

    def jade_username(self) -> str:
        return self._jade_username

    def set_keyring_file(self, keyring_file) -> str:
        self._keyring_file = keyring_file

    def set_private_key_file(self, private_key_file):
        self._private_key_file = private_key_file

    def set_jade_hostname(self, jade_hostname):
        self._jade_hostname = jade_hostname

    def set_jade_username(self, jade_username) -> None:
        self._jade_username = jade_username


    @staticmethod
    def from_dict(val):
        config = Config()
        config.set_keyring_file(val.get('keyring_file'))
        config.set_private_key_file(val.get('private_key_file'))
        config.set_jade_hostname(val.get('jade_hostname'))
        config.set_jade_username(val.get('jade_username'))
        return config

    def to_dict(self):
        return {
            'keyring_file': self.keyring_file(),
            'private_key_file': self.private_key_file(),
            'jade_hostname': self.jade_hostname(),
            'jade_username': self.jade_username(),
        }
