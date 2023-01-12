import paramiko
import select
import time

from jade_front.common.config import Config

class AbstractAPI:
    def __init__(self):
        self._config = Config.instance()

    def ssh_connection(self):
        k = paramiko.RSAKey.from_private_key_file(self._config.private_key_file())
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=self._config.jade_hostname(),
            username=self._config.jade_username(),
            pkey=k,
            timeout=6 * 10e4,
        )
        return ssh

    def run_api(self, command):
        ssh_connection = self.ssh_connection()
        ssh_stdin, ssh_stdout, ssh_stderr = ssh_connection.exec_command(command)
        outputs = ssh_stdout.readlines()
        return outputs
