from search.searcher import search
from search.indexer import InvertedIndex

def test_and_search():

    index = InvertedIndex()
    index.add_document("doc1.txt", "error crash system")
    index.add_document("doc2.txt", "crash system reboot")

    result = search("error crash", index)
    assert "doc1.txt" in result
    assert "doc2.txt" not in result

def test_search_empty():
    
    index = InvertedIndex()
    result = search("nothing", index)
    assert result == {}


