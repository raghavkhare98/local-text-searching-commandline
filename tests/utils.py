from search.indexer import InvertedIndex

def make_index(documents):
    index = InvertedIndex()
    for filename, content in documents.items():
        index.add_document(filename, content)
    return index