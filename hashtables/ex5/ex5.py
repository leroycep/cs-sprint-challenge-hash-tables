
def get_file_name(filepath):
    last_slash = filepath.rfind("/");
    if last_slash == -1:
        return filepath
    else:
        return filepath[last_slash+1:]

def finder(files, queries):
    # This is a hash map that stores a list of file_names -> file_paths
    name_to_paths = {}
    for filepath in files:
        file_name = get_file_name(filepath)
        if file_name in name_to_paths:
            name_to_paths[file_name].append(filepath)
        else:
            name_to_paths[file_name] = [filepath]
    results = []
    for query in queries:
        if query in name_to_paths:
            results.extend(name_to_paths[query])
    return results


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
