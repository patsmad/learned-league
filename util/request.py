from bs4 import BeautifulSoup as BS
from requests import get
import json
import os

file_path = os.path.dirname(os.path.realpath(__file__))
data_path = '{}/../'.format(file_path)
with open(data_path + 'config/config.json', 'r') as f:
    headers = json.load(f)['headers']

def retryGet(url, retry, cache=True):
    if retry < 5:
        try:
            if not cache:
                headers['Cache-Control'] = 'no-cache'
            out = get(url, timeout=60.0, headers=headers)
            return out
        except:
            print("Retry")
            return retryGet(url, retry + 1, cache)
    else:
        raise Exception("ABORT")

def soupifyURL(url, cache=True):
    with requestURL(url, cache) as request:
        return BS(request.text, 'html.parser')

def requestURLText(url, cache=True):
    with requestURL(url, cache) as request:
        return request.text

def requestURL(url, cache=True):
    return retryGet(url, 0, cache)
