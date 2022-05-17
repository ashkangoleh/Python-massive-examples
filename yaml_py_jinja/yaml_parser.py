import yaml
import os
from jinja2 import FileSystemLoader,Environment
import json

file_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.full_load(open(f"{file_dir}/input.yaml"))


env = Environment(loader=FileSystemLoader(f"{file_dir}"),trim_blocks=True,lstrip_blocks=True)
template = env.get_template('print.j2')


print(template.render(config))


with open(f"{file_dir}/test.py","w") as f:
        f.write(template.render(config))
        
        
# for filename in os.listdir(file_dir):
#     if filename.endswith('.yaml'):
#         with open(f"{file_dir}/{filename}", "r") as stream:
#             try:
#                 yaml_data = yaml.safe_load(stream)
#                 # print(json.dumps(yaml_data, indent=4))
#                 for k,v in yaml_data.items():
#                     print(','.join(v['description']))
#                 # name = yaml_data['employee_1']
#                 # name['Name'] = 'Ashkan'
#                 # for k,v in name.items():
#                 #     print(f"{k}= {v}")
#             except FileNotFoundError as e:
#                 raise e
