import requests


def detect():
    ip = "167.235.26.156"
    url = f"https://vpnapi.io/api/{ip}?key=05385225f52441409cf65ebecf651584"
    res = requests.get(url)
    return res.json()



print("==>> detect(): ", detect())