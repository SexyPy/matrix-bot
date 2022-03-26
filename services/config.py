import yaml

class Config:
    def __init__(self) -> None:
        self.config_file = "config.yaml"

    def get_config(self):
        with open(self.config_file, "r") as yml_file:
            return yaml.safe_load(yml_file)
