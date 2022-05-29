import json
from datetime import datetime

BASE_URL = 'https://localhost:7676'


def get_code_samples(route, method):
    now = str(datetime.now().strftime("%Y-%m-%d"))
    nl = '\n'  # new line character to use in f-strings.
    if method in ['POST', 'PUT', 'DELETE'] and route.body_field:
        print(f"Path:{route.path}")
        try:
            example_schema = route.body_field.type_.Config.schema_extra.get('example')
            payload = f"json.dumps({example_schema})"
            data_raw = f"\\{nl} --data-raw " + "'" + f"{json.dumps(example_schema)} " + "'"
            params = {'since': '2009-01-01', 'until': f'{now}', 'page_num': 1, 'page_size': 10}
        except Exception as e:
            print(f"Path:{route.path} Error:{e}")
            payload = '{}'
            data_raw = ''
            params = {'since': '2009-01-01', 'until': f'{now}', 'page_num': 1, 'page_size': 10}
    else:
        payload = '{}'
        data_raw = ''
        params = {'since': '2009-01-01', 'until': f'{now}', 'page_num': 1, 'page_size': 10}
    return [
        {
            'lang': 'Shell',
            'source': f"curl -X 'GET'\\{nl} "
                      f"'{BASE_URL}{route.path}?page_num=1&page_size=10&since=2009-01-03&until={now}'\\{nl} "
                      f"-H 'accept: application/json'"
                      f"{data_raw}",
            'label': 'Shell'
        },
        {
            'lang': 'Python',
            'source': f"import requests{nl}"
                      f"{'import json' + nl if method.lower() == 'post' else ''}{nl}"
                      f"url = \"{BASE_URL}{route.path}\"{nl}"
                      f"params = {params}{nl}"
                      f"response = requests.get(url=url, params=params){nl}"
                      f"print(response.json())",
            'label': 'Python3'
        },
        {
            'lang': 'JavaScript',
            'source': f"fetch('{BASE_URL}{route.path}?page_num=1&page_size=10&since=2009-01-03&until={now}'){nl}"
                      f".then(response => response.json()){nl}"
                      ".then(data => console.log(data))",
            'label': 'JavaScript'
        },
        {
            'lang': 'NodeJs',
            'source': f"require('axios'){nl}"
                      f".get('{BASE_URL}{route.path}?page_num=1&page_size=10&since=2009-01-03&until={now}'){nl}"
                      f".then(response => console.log(response))",
            'label': 'NodeJs'
        },
        {
            'lang': 'Ruby',
            'source': f"require 'net/http'{nl}"
                      f"uri = URI('{BASE_URL}{route.path}?page_num=1&page_size=10&since=2009-01-03&until={now}'){nl}"
                      f"puts Net::HTTP.get(uri)",
            'label': 'Ruby'
        },
        {
            'lang': 'Go',
            'source': f"import ({nl}"
                      f"    io/ioutil{nl}"
                      f"    log{nl}"
                      f"    net/http{nl}"
                      f"    ){nl}"
                      f"resp, err := http.Get('{BASE_URL}{route.path}?page_num=1&page_size=10&since=2009-01-03&until={now}'){nl}"
                      "if err != nil { \n log.Fatalln(err) \n}",
            'label': 'Go'
        },
    ]
