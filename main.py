"""Contains function for creating random headers, including user-agent"""
from fake_useragent import UserAgent, FakeUserAgentError
from fake_headers.headers import gen_headers


def make_headers(browser: str = 'random'):
    """Browsers: chrome, opera, ie, firefox, safari"""
    ua = UserAgent()
    try:
        browser = ua[browser]
    except (KeyError, FakeUserAgentError):
        print('Warning, not correct browser')
        browser = ua.random

    return gen_headers(browser)


if __name__ == '__main__':
    print(make_headers())
