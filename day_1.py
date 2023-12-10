from common import wrapper


@wrapper
def solve_p1(data, *_):
    """
    Solve d1p1
    """
    data = [
        [x if x not in "abcdefghijklmnopqrtstuvwxyz\n" else None for x in y]
        for y in data
    ]
    data = [
        [
            list(filter(lambda x: x is not None, x))[0],
            list(filter(lambda x: x is not None, x))[-1],
        ]
        for x in data
    ]
    data = [int("".join(x)) for x in data]
    return sum(data)


@wrapper
def solve_p2(data, *_):
    """
    Solve d1p2
    """
    digits = {
        "one": "on1ne",
        "two": "tw2wo",
        "three": "thr3ree",
        "four": "fou4our",
        "five": "fiv5ive",
        "six": "si6ix",
        "seven": "sev7ven",
        "eight": "eig8ght",
        "nine": "nin9ine",
    }
    for index, datapoint in enumerate(data):
        for digit, replacement in digits.items():
            datapoint = datapoint.replace(digit, replacement)
            data[index] = datapoint

    return solve_p1(data)


print(solve_p1("data/day_1.txt"))
print(solve_p2("data/day_1.txt"))
