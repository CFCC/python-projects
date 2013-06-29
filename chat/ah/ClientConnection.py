# AH
class Client:
    def __init__(self, username, ip):
        self.username = username
        self.ip = ip
        if self.ip == "127.0.0.1":
            self.is_admin = True
        else:
            self.is_admin = False
