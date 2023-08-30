import requests


def apple_input(url, word):
    res = requests.get(url + word)
    return 'meanings' in res.text and res.status_code < 400


def run_input(url, word):
    res = requests.get(url + word)
    data = res.text.count('definitions')
    counter = 0
    if data > 2:
        counter += 1
        return counter and res.status_code < 400


def asdfghjkl_input(url, word):
    res = requests.get(url + word)
    return 'No Definitions Found' in res.text and res.status_code >= 400


def book_in_spanish_n(url, word):
    res = requests.get(url + word)
    return "No Definitions Found" in res.text and res.status_code >= 400