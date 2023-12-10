from common import wrapper, transpose
import re


@wrapper
def solve_p1(data, *args, **kwargs):
    games = []
    bag = [12,14,13]
    for datapoint in data:
        datapoint = re.sub("Game \d+: ", "",datapoint)
        datapoint = datapoint.split(";")
        datapoint = [x if "red" in x else x+", 0 red" for x in datapoint]
        datapoint = [x if "green" in x else x + ", 0 green" for x in datapoint]
        datapoint = [x if "blue" in x else x + ", 0 blue" for x in datapoint]
        datapoint = [x.split(", ")for x in datapoint]
        datapoint = [sorted(x, key=lambda x:x[-1]) for x in datapoint]
        datapoint = [[[z if z not in "abcdefghijklmnopqrtstuvwxyz" else None for z in y] for y in x]for x in datapoint]
        datapoint = [[int("".join(list(filter(lambda x:x is not None, y))).replace(" ", "")) for y in x]for x in datapoint]
        datapoint = transpose(datapoint)  # R B G
        datapoint = [max(x) for x in datapoint]
        games.append(datapoint)
    games = list(map(lambda x: all([x[i] <= bag[i] for i in range(len(x))]), games))
    games = list(zip(games, range(1,len(games)+1)))
    games = [x[0] * x[1] for x in games]
    return sum(games)

@wrapper
def solve_p2(data, *args, **kwargs):
    games = []
    for datapoint in data:
        datapoint = re.sub("Game \d+: ", "",datapoint)
        datapoint = datapoint.split(";")
        datapoint = [x if "red" in x else x+", 0 red" for x in datapoint]
        datapoint = [x if "green" in x else x + ", 0 green" for x in datapoint]
        datapoint = [x if "blue" in x else x + ", 0 blue" for x in datapoint]
        datapoint = [x.split(", ")for x in datapoint]
        datapoint = [sorted(x, key=lambda x:x[-1]) for x in datapoint]
        datapoint = [[[z if z not in "abcdefghijklmnopqrtstuvwxyz" else None for z in y] for y in x]for x in datapoint]
        datapoint = [[int("".join(list(filter(lambda x:x is not None, y))).replace(" ", "")) for y in x]for x in datapoint]
        datapoint = transpose(datapoint)  # R B G
        datapoint = [max(x) for x in datapoint]
        games.append(datapoint)
    games = [x[0]*x[1]*x[2] for x in games]
    return sum(games)

print(solve_p1("data/day_2.txt"))
print(solve_p2("data/day_2.txt"))
