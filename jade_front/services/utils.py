import base64


def encode_decode_zip(file_string):
    file_string = file_string.strip('data:application/zip;base64,')
    file_binary = file_string.strip().encode()
    file_binary = base64.b64decode(file_binary)
    return file_binary