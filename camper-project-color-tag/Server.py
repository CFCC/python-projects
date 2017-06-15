import socket
import _thread

s = socket.socket()
s.bind((socket.gethostname(), 10000))
version = "1.0"

