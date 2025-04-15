from search.indexer import InvertedIndex

def test_inverted_index_single_doc():
    index = InvertedIndex()

    index.add_document("doc1.txt", "hello world hello")

    assert index.lookup("hello") == {"doc1.txt": [0,2]}
    assert index.lookup("world") == {"doc1.txt": [1]}
    assert index.lookup("missing") == {}

def test_inverted_index_multiple_docs():

    index = InvertedIndex()

    index.add_document("doc2.txt", "apple banana")
    index.add_document("doc3.txt", "banana carrot apple")

    appleHits = index.lookup("apple")
    assert "doc2.txt" in appleHits
    assert "doc3.txt" in appleHits

