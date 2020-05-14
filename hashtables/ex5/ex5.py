def finder(files, queries):

    """
    YOUR CODE HERE
    """
    
    d = {}
    result = []

    for f in files:
        path_arr = f.split('/')
        if path_arr[-1] not in d:
            d[path_arr[-1]] = []
        d[path_arr[-1]].append(f)

    for q in queries:
        if q in d:
            for path in d[q]:
                result.append(path)

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
