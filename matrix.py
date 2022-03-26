from services.account import Account
from services.config import Config

class MatrixPy:
        def __init__(self) -> None:
            self.version  = "1.0.0"
            self.config = Config().get_config()
            self.account = Account(self.config)

        def get_version(self):
            return self.version

        def login(self):
            return self.account.data


if __name__ == '__main__':
    matrix = MatrixPy()
    print(matrix.login())
