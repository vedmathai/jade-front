import paramiko
import select

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
            pkey=k
        )
        return ssh

    def run_api(self, command):
        ssh_connection = self.ssh_connection()
        ssh_stdin, ssh_stdout, ssh_stderr = ssh_connection.exec_command(command)
        outputs = []
        while not ssh_stdout.channel.exit_status_ready():
            # Only print data if there is data to read in the channel
            if ssh_stdout.channel.recv_ready():
                rl, wl, xl = select.select([ssh_stdout.channel], [], [], 0.0)
                if len(rl) > 0:
                    tmp = ssh_stdout.channel.recv(1024**2)
                    outputs.append(tmp.decode())
        return outputs

    def upload_file(self, local_filepath, remote_filepath):
        ssh = self.ssh_connection()
        sftp_client = ssh.open_sftp()
        sftp_client.put(local_filepath, remote_filepath)
        sftp_client.close()

    def download_file(self, remote_filepath, local_filepath):
        ssh = self.ssh_connection()
        sftp_client = ssh.open_sftp()
        sftp_client.get(remote_filepath, local_filepath)
        sftp_client.close()
