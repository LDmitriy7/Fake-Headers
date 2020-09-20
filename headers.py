"""Contains kit of various headers"""
from random import choice, random

all_headers = {
    'Accept-Charset': ['utf-8'],
    'Connection': ['keep-alive', 'close'],
    'Accept-Encoding': ['gzip, deflate, br'],
    'Accept-Language': ['en-US;q=0.5,en;q=0.3', 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'],
    'Cache-Control': ['max-age=0', 'no-cache', 'no-store'],
    'Referer': ['https://google.com', 'https://yandex.ru'],
    'Pragma': ['no-cache'],
    'DNT': ['1'],
    'Upgrade-Insecure-Requests': ['1'],
}


def gen_headers(browser: str) -> dict:
    """Generates random headers; user-agent: browser"""
    new_headers = {}
    for name, values in all_headers.items():
        if random() > 0.3:
            new_headers[name] = choice(values)
    new_headers['User-Agent'] = browser
    new_headers['Accept'] = choice(['*/*', 'text/plain', 'text/html', 'application/xhtml+xml'])
    return new_headers
