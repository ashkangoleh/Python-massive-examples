import yaml
import os
from jinja2 import FileSystemLoader,Environment
import json

file_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.full_load(open(f"{file_dir}/input.yaml"))
print('config: ', config)


env = Environment(loader=FileSystemLoader(f"{file_dir}"),trim_blocks=True,lstrip_blocks=True)
template = env.get_template('print.j2')

body = {"name":["majid","ashkan","asghar",'pp'],"x":2,"y":12}

# print(template.render(config))
print(template.render(body))


# with open(f"{file_dir}/test2.py","w") as f:
#         f.write(template.render(config))
        
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
