from jade_front.jade_api.apis.abstract_api import AbstractAPI


class DownloadFileAPI(AbstractAPI):

    def download_file(self, remote_filepath, local_filepath):
        ssh = self.ssh_connection()
        sftp_client = ssh.open_sftp()
        sftp_client.get(remote_filepath, local_filepath)
        sftp_client.close()
