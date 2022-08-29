import requests
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))
from print_response import print_response

# https://pokeapi.co/api/v2


def main():
    count = 1
    url = 'http://pokeapi.co/api/v2/pokemon'
    headers = {'Accept': 'application/json'}
    params = {
        "limit": 200
    }
    resp = requests.get(url, headers=headers,params=params)
    resp.raise_for_status()
    
    data = resp.json()
    breakpoint()
    while data['next']:
        resp = requests.get(data['next'], headers=headers)
        resp.raise_for_status() 
        count +=1
        print_response(resp, filename=f"pokemon/get_all_pokemon_{count}")
        data = resp.json()
        
    # for pokemon in resp.json()['results']:
    #     resp = requests.get(pokemon['url'], headers=headers)
    #     breakpoint()
    #     if resp.ok:
    #         print_response(
    #             resp, filename=f"/python_extra/req/pokemon/get_{pokemon['name']}")
    #     else:
    #         print(f"could not load {pokemon['name']} details")


if __name__ == '__main__':
    main()
