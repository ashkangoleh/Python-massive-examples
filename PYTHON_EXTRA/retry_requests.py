import requests
import random
from retry import retry

# Read proxies from file
with open('proxies.txt', 'r') as file:
    proxies_list = file.readlines()

# Clean the proxies list
proxies_list = [proxy.strip() for proxy in proxies_list]

# Shuffle the list of proxies
random.shuffle(proxies_list)

# Retry function
@retry(tries=3, delay=2, backoff=2, jitter=(1, 3), predicate=lambda r: r.status_code in [403, 404])
def send_request(proxy_url):
    proxy = {'http': 'http://' + proxy_url, 'https': 'https://' + proxy_url}
    try:
        # Send the request
        response = requests.get('http://example.com', proxies=proxy)
        print(response.text)
    except:
        print(f"Proxy {proxy} is not working")
        raise
    return response

for proxy_url in proxies_list:
    send_request(proxy_url)
