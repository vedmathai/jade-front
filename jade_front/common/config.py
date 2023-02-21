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
        self._database_name = None
        self._database_schema_file = None

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

    def database_name(self) -> str:
        return self._database_name

    def database_schema_file(self) -> str:
        return self._database_schema_file

    def remote_projects_folder_name(self) -> str:
        return self._remote_projects_folder_name

    def remote_projects_code_folder_name(self) -> str:
        return self._remote_projects_code_folder_name

    def remote_projects_code_file_name(self) -> str:
        return self._remote_projects_code_file_name

    def remote_projects_data_folder_name(self) -> str:
        return self._remote_projects_data_folder_name

    def remote_projects_data_file_name(self) -> str:
        return self._remote_projects_data_file_name

    def set_keyring_file(self, keyring_file) -> str:
        self._keyring_file = keyring_file

    def set_private_key_file(self, private_key_file):
        self._private_key_file = private_key_file

    def set_jade_hostname(self, jade_hostname):
        self._jade_hostname = jade_hostname

    def set_jade_username(self, jade_username) -> None:
        self._jade_username = jade_username

    def set_database_name(self, database_name) -> None:
        self._database_name = database_name

    def set_database_schema_file(self, database_schema_file) -> str:
        self._database_schema_file = database_schema_file

    def set_remote_projects_folder_name(self, remote_projects_folder_name) -> str:
        self._remote_projects_folder_name = remote_projects_folder_name

    def set_remote_projects_code_folder_name(self, remote_projects_code_folder_name) -> None:
        self._remote_projects_code_folder_name = remote_projects_code_folder_name

    def set_remote_projects_code_file_name(self, remote_projects_code_file_name) -> None:
        self._remote_projects_code_file_name = remote_projects_code_file_name

    def set_remote_projects_data_folder_name(self, remote_projects_data_folder_name) -> None:
        self._remote_projects_data_folder_name = remote_projects_data_folder_name

    def set_remote_projects_data_file_name(self, remote_projects_data_file_name) -> None:
        self._remote_projects_data_file_name = remote_projects_data_file_name


    @staticmethod
    def from_dict(val):
        config = Config()
        config.set_keyring_file(val.get('keyring_file'))
        config.set_private_key_file(val.get('private_key_file'))
        config.set_jade_hostname(val.get('jade_hostname'))
        config.set_jade_username(val.get('jade_username'))
        config.set_database_name(val.get('database_name'))
        config.set_database_schema_file(val.get('database_schema_file'))
        config.set_remote_projects_folder_name(val.get('remote_projects_folder_name'))
        config.set_remote_projects_code_folder_name(val.get('remote_projects_code_folder_name'))
        config.set_remote_projects_code_file_name(val.get('remote_projects_code_file_name'))
        config.set_remote_projects_data_folder_name(val.get('remote_projects_data_folder_name'))
        config.set_remote_projects_data_file_name(val.get('remote_projects_data_file_name'))
        return config

    def to_dict(self):
        return {
            'keyring_file': self.keyring_file(),
            'private_key_file': self.private_key_file(),
            'jade_hostname': self.jade_hostname(),
            'jade_username': self.jade_username(),
            'database_name': self.database_name(),
            'database_schema_file': self.database_schema_file(),
            'remote_projects_folder_name': self.remote_projects_folder_name(),
            'remote_projects_code_folder_name': self.remote_projects_code_folder_name(),
            'remote_projects_code_file_name': self.remote_projects_code_file_name(),
            'remote_projects_data_folder_name': self.remote_projects_data_folder_name(),
            'remote_projects_data_file_name': self.remote_projects_data_file_name(),
        }
