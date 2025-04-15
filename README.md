Description:

Indexes and searches through local `.txt` and `.log` files using a custom inverted index.

How it works:
- Crawler collects all files mentioned in the function arguments. Specify file type by using '.extension'
Example - '.md'
- Tokenizer normalizes and splits text. It does so by using regular expression and matches all patterns which match the text ('\w+')
- Inverted index maps tokens to file locations
- Query engine supports AND / PHRASE search
