#pip install python-box
from box import Box
import yaml
import json


config = Box.from_yaml(filename="/external/test_proj/PYTHON_EXTRA/python_config_reader/config.yaml",Loader=yaml.FullLoader)


print(json.dumps(dict(config.items()),indent=4))