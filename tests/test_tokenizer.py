from search.tokenizer import tokenize

def test_tokenize():
    text = "Hello, World! This is a test"
    tokens = tokenize(text)
    assert tokens == ['hello', 'world', 'this', 'is', 'a', 'test']
