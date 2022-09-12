import requests
import logging
import pdb

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S',
    level=logging.INFO
    # level=logging.INFO
)
logger = logging.getLogger()
# breakpoint()

my_headers = {"Accept": "text/html"}
params = {"limit": 5, "type": "tech"}
body = {"name": "nick", "kids": 2}
resp = requests.get('http://njrusmc.net', params=params,
                    headers=my_headers, data=body)

logger.info(f"{resp.status_code}/{resp.reason}")
print(f"Result: {resp.status_code}/{resp.reason}", end=f"\n{'*'*50}\n")

print(
    f"Header content type: {resp.headers['Content-Type']}", end=f"\n{'*'*50}\n")

print(resp.request.body, end=f"\n{'*'*50}\n")

print(f"path url : {resp.request.path_url}", end=f"\n{'*'*50}\n")

print(f"full request url: {resp.request.url}", end=f"\n{'*'*50}\n")
# print(resp.text)
print(f"reason of status code : {resp.reason}", end=f"\n{'*'*50}\n")

# print(help(requests))
# print(help(requests.api))
print(dir(resp), end=f"\n{'*'*50}\n")
print(resp.raise_for_status(), end=f"\n{'*'*50}\n")
print(f"number of redirects(if any exist print out the URL/status){resp.history}", end=f"\n{'*'*50}\n")

print(f"Elapsed time(second): {resp.elapsed.seconds} s", end=f"\n{'*'*50}\n")
print(f"Elapsed time(us): {resp.elapsed.microseconds} us", end=f"\n{'*'*50}\n")
