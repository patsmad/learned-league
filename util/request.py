from bs4 import BeautifulSoup as BS
from requests import get
from util.data_cache import openJson

headers = openJson('config/config.json')['headers']

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
