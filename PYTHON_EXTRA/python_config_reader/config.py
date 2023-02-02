from pathlib import Path
import json
from dataclasses import dataclass


@dataclass
class Config:
    somthing_test: bool = True
    somthing_different: bool = True


def read_config_file() -> Config:
    config_file = Path.cwd() / 'PYTHON_EXTRA/python_config_reader/config.json'
    print("==>> config_file: ", config_file)
    config_dict = json.loads(config_file.read_text())
    return Config(**config_dict)


config = read_config_file()
w = True
print(w == config.somthing_test)
print("==>> config: ", config)
