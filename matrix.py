from services.account import Account
from services.config import Config
import signal
import time

class MatrixPy:
        def __init__(self) -> None:
            self.config = Config().get_config()
            self.account = Account(self.config)

        def get_version(self):
            return self.config["version"]

        def login(self):
            return self.account.data

        def logout(self):
            self.account.close()
            exit(0)

        def handler(self, signum, frame):
            self.logout()

if __name__ == '__main__':
    matrix = MatrixPy()
    login = matrix.login()

    signal.signal(signal.SIGINT, matrix.handler)

    while True:
        time.sleep(0.1)