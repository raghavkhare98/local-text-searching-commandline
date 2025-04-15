from search.crawler import read_files
from search.indexer import InvertedIndex
from search.searcher import search
from config import DEFAULT_EXTENSIONS

def run_search(path, query):
    
    files = read_files(path, extensions=DEFAULT_EXTENSIONS)
    index = InvertedIndex()

    for filename, content in files.items():
        index.add_document(filename, content)
    
    results = search(query, index)
    
    return results