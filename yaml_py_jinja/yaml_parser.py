import jinja2
import yaml
import os
from jinja2 import FileSystemLoader, Environment
import json

file_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.full_load(open(f"{file_dir}/input.yaml"))
config2 = yaml.full_load(open(f"{file_dir}/different_form_yaml.json"))

env = Environment(loader=FileSystemLoader(
    f"{file_dir}"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('print.j2')
# html_ = env.get_template('ht.html').render(content=config2)
dump_ = env.get_template('print.j2').render(content=config2)
dump_1 = env.get_template('print.j2').render(code=config2)
# body = {"name": ["majid", "ashkan", "asghar", 'pp'], "x": 2, "y": 12}
dumps = {"dump_": dump_, "dump_1": dump_1}

# print(template.render(body))
# convert json to yml
# ff = open(f'{file_dir}/meta.yaml', 'w+')
# print(yaml.dump(config2,ff,allow_unicode=True))
# json to html
# with open(f"{file_dir}/test_html.html","w") as f:
#         f.write(dump_)
# json to python
for k,v in dumps.items():
        with open(f"{file_dir}/{k}.py", "w+") as f:
                f.write(v)

# with open(f"{file_dir}/test2.py","w") as f:
#         f.write(template.render(body))

# for filename in os.listdir(file_dir):
#     if filename.endswith('.yaml'):
#         with open(f"{file_dir}/{filename}", "r") as stream:
#             try:
#                 yaml_data = yaml.safe_load(stream)
#                 print(json.dumps(yaml_data, indent=4))
#                 # for k,v in yaml_data.items():
#                 #     print(k,v)
#                 # name = yaml_data['employee_1']
#                 # name['Name'] = 'Ashkan'
#                 # for k,v in name.items():
#                 #     print(f"{k}= {v}")
#             except FileNotFoundError as e:
#                 raise e
