import pytest

from ..search import Search

def test_builtLink_google():
    tempSearch = Search()
    tempSearch.setEngine("twitter")
    tempSearch.setDomain("com")
    tempSearch.setQuery(["test","query"])
    assert tempSearch.buildLink() == "http://www.twitter.com/search?q=test query"
