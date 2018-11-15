import pytest

from ..search import Search


def test_builtLink_google():
    tempSearch = Search()
    tempSearch.setEngine("google")
    tempSearch.setDomain("com")
    tempSearch.setQuery(["test","query"])
    assert tempSearch.buildLink() == "http://www.google.com/search?q=test+query"
