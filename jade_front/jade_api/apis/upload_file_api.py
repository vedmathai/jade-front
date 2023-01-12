from jade_front.jade_api.apis.abstract_api import AbstractAPI


class UploadFileAPI(AbstractAPI):

    def upload_file(self, local_filepath, remote_filepath):
        ssh = self.ssh_connection()
        sftp_client = ssh.open_sftp()
        sftp_client.put(local_filepath, remote_filepath)
        sftp_client.close()
