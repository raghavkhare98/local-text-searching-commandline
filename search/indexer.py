from collections import defaultdict
from search.tokenizer import tokenize

class InvertedIndex:
    def __init__(self):
        """
        a 2d dictionary because we are creating new keys for each new word, the second level of the
        dictionary will contain the document name as the key and it's value will be the position of the word
        """
        self.index = defaultdict(lambda: defaultdict(list))
    
    #this function will populate the 2d dictionary
    def add_document(self, fileName, text):

        token = tokenize(text)
        for position, token in enumerate(token):
            self.index[token][fileName].append(position)
    
    def lookup(self, token):

        return self.index.get(token, {})