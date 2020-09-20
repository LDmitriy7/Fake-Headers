# Fake-Headers
Generator of User-Agent and other headers for http requests. Without internet requests.

## Required
`pip install fake_useragent`



## Example
- Code:  
```python
from fake_headers import make_headers
from pprint import pprint

headers = make_headers('chrome')
headers2 = make_headers()

pprint(headers)
pprint(headers2)
```

- Output:  
```
{'Accept': 'text/html',
 'Accept-Charset': 'utf-8',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
 'Cache-Control': 'max-age=0',
 'Pragma': 'no-cache',
 'Referer': 'https://yandex.ru',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
               'like Gecko) Chrome/33.0.1750.517 Safari/537.36'}

{'Accept': 'text/plain',
 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
 'Cache-Control': 'no-store',
 'Connection': 'keep-alive',
 'DNT': '1',
 'Pragma': 'no-cache',
 'Referer': 'https://google.com',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like '
               'Gecko) Chrome/36.0.1985.67 Safari/537.36'}
```
