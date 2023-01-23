from socket import socket
from gmpy2 import iroot
from time import sleep

def read(sock):
    sleep(0.1)
    return sock.recv(4000).decode()

with socket() as s:
    s.connect(("security-challenge.bmw-carit.de", 21042))
    read(s)                                                 # get Certificate selection
    s.send(b'1\n')                                          # send Cert Number 1
    challenge = read(s).split('\n')[-2][10:]                # get Challenge
    nonce = str(iroot(int(challenge),3)[0])                 # calc cube root of Challenge
    s.send(nonce.encode()+b'\n')                            # send Nonce
    print(read(s))                                          # get flag
