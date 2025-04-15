import re

def tokenize(text):
    return re.findall(r'\w+', text.lower())

# print(tokenize('Where do I even begin?'))