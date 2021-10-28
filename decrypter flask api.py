from binascii import unhexlify, hexlify
import pyaes
from flask import Flask
app = Flask(__name__)


@app.route('/decrypt/<arg1>')
def MyFunc(arg1):
    #AES-256 CBC
    #openssl enc -nosalt -aes-256-cbc -k hello-aes -P
    msg = unhexlify(arg1)
    key = unhexlify("E8B6C00C9ADC5E75BB656ECD429CB1643A25B111FCD22C6622D53E0722439993")
    iv = unhexlify("E486BB61EB213ED88CC3CFB938CD58D7")
    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv = iv))
    decrypted = decrypter.feed(msg)
    decrypted += decrypter.feed()
    return decrypted