import pytest
from APIFunctions import *


class TestZiv:
    @pytest.fixture()
    def url(self):
        return 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def test_apple_input(self, url, word="apple"):
        actual = apple_input(url, word)
        assert actual, 'Give correct response, and information on apple word'

    def test_run_input(self, url, word="run"):
        actual = run_input(url, word)
        assert actual, 'give correct response and multiple definitions of the word run'

    def test_asdfghjkl_input(self, url, word="asdfghjkl"):
        actual = asdfghjkl_input(url, word)
        assert actual, 'No Definitions Found'


@pytest.fixture()
def spanish_url():
    return 'https://api.dictionaryapi.dev/api/v2/entries/es/'


class TestZivSpanish:

    def test_book_in_spanish_n(self, spanish_url, word='book'):
        actual = book_in_spanish_n(spanish_url, word)
        assert actual, 'Cannot find meaning in spanish'
