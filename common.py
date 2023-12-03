import os

def wrapper(f):
    def inner(*args, **kwargs):
        if args:
            if isinstance(args[0], str) and os.path.exists(args[0]) and os.path.isfile(args[0]):
                with open(args[0]) as file:
                    data = file.readlines()
                    data = list(map(lambda x: x.strip("\n"), data))
                args = (data, args[1:])
        return f(*args, **kwargs)

    return inner

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]