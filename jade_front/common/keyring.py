import json


from jade_front.common.config import Config

class Keyring:
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def instantiate() -> None:
        config = Config.instance()
        keyring_file = config.keyring_file()
        with open(keyring_file, 'rt') as f:
            keyring = Keyring.from_dict(json.load(f))
        Keyring._instance = keyring

    @staticmethod
    def instance() -> "Keyring":
        if Keyring._instance is None:
            raise Exception('Keyring not instantiated, use Keyring.instantiate() function first')  # noqa
        return Keyring._instance

    @staticmethod
    def from_dict(val):
        keyring = Keyring()
        return keyring

    def to_dict(self):
        return {
        }
