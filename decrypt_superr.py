import sys

from cryptography.fernet import Fernet
import base64
password_superr = b'~\xb1\xf2\xe0\xbf\x06\x11X\xad]x\x05\xc4\xdd4\x8c|\x867\xb4\x1a\x84\xf8\xaa\xfa\x82c\x9f\xdf\xe3\xc4#'
def get_token(filename):
    data = b''
    with open(filename, "rb") as f:
        while True:
            f_read = f.read(2)
            if len(f_read) == 0:
                break
            if len(f_read) == 1:
                f_read += b'\x00'
            data += f_read[:1]
    return data.decode('utf8')
def decrypt(token, password):
    decrypter = Fernet(password)
    decrypted = decrypter.decrypt(token)
    return decrypted
if __name__ == '__main__':
    decrypted_data  = decrypt(get_token(sys.argv[1]), base64.b64encode(password_superr))
    with open(sys.argv[1]+".py", 'wb') as f:
        f.write(decrypted_data)
    print('Decrypted data saved to {}'.format(sys.argv[1]+".py"))