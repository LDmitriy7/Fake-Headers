"""Contains kit of various headers"""
from random import choice, random

all_headers = {
    'Accept': ['*/*', 'text/plain', 'text/html', 'application/xhtml+xml',
               'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'],
    'Accept-Charset': ['utf-8'],
    'Accept-Encoding': ['gzip, deflate, br'],
    'Accept-Language': ['en-US;q=0.5,en;q=0.3', 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'],
    'Cache-Control': ['max-age=0', 'no-cache', 'no-store'],
    'Referer': ['https://google.com', 'https://yandex.ru'],
    'Pragma': ['no-cache'],
    'DNT': ['1'],
    'Upgrade-Insecure-Requests': ['1'],
    'Content-Type': ['text/ping'],
    'Sec-Fetch-Dest': ['document'],
    'Sec-Fetch-Mode': ['navigate'],
    'Sec-Fetch-Site': ['cross-site'],
    'Sec-Fetch-User': ['?1'],
}


def gen_headers(browser: str) -> dict:
    """Generates random headers; user-agent: browser"""
    new_headers = {}
    for name, values in all_headers.items():
        if random() > 0.2:
            new_headers[name] = choice(values)
    new_headers['User-Agent'] = browser
    return new_headers
