def group_by_owners(files):
    d = {}
    for k, v in files.items():
        if v in d.keys():
            d[v].append(k)
        else:
            d[v] = [k]
    return d

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))