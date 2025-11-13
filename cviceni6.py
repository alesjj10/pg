import sys
import requests
import json


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} prefix')
        sys.exit

    prefix = sys.argv[1]
    url = f'https://data.carnewschina.com/suggest?q={prefix}'

    response = requests.get(url)
    if not response.ok:
        sys.exit()

#    data = json.load(response.text)
    data = response.json

    for model in data['models']:
        print(model['name'])



