def search(query, index):
    
    tokens = query.lower().split()
    if not tokens:
        return {}

    #we will start the search with the first term
    result = index.lookup(tokens[0])

    if len(tokens) > 1:
        for token in tokens[1:]:
            tokenResults = index.lookup(token)
            commonFiles = set(result.keys()) & set(tokenResults.keys())
            result = {file: result[file] for file in commonFiles}

    return result