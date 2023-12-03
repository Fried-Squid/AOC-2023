from common import wrapper, transpose
import re

@wrapper
def solve_p1(data, *args, **kwargs):
    games = []
    for datapoint in data:
        datapoint = re.sub("Game \d+: ", "",datapoint)
        datapoint = datapoint.split(";")
        #too fucked rn


        games.append(res)
    return sum(list(map(lambda x:games.index(x), games)))

print(solve_p1("data/day_2.txt"))
