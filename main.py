"""Contains function for creating random headers, including user-agent"""
from fake_useragent import UserAgent, FakeUserAgentError
from headers import gen_headers


def make_headers(browser: str = 'random'):
    """Browsers: chrome, opera, ie, firefox, safari"""
    ua = UserAgent()
    try:
        browser = ua[browser]
    except (KeyError, FakeUserAgentError):
        print('Warning, not correct browser')
        browser = ua.random

    return gen_headers(browser)
