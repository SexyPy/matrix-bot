import urllib3
import json

class Account:
    def __init__(self, config: json) -> None:
        self.http = urllib3.PoolManager()
        self.config = config

        self.endpoints = {
            "login": f"https://{self.config['hostname']}/_matrix/client/r0/login"
        }

        self.data: dict = self.request_login()


    def request_login(self):
        json_data = {
            'type': 'm.login.password',
            'password': self.config["credentials"]["password"],
            'identifier': {
                'type': 'm.id.user',
                'user': self.config["credentials"]["username"],
            },
            'initial_device_display_name': 'Matrix Bot',
        }

        return json.loads(self.http.request("POST", self.endpoints["login"], body = json.dumps(json_data)).data.decode())
