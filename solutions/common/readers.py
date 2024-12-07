def read_strings(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def read(file_path):
    with open(file_path) as f:
        return f.read()