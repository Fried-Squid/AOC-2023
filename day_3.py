from common import wrapper

def solve_p1(data, *args, **kwargs):
    data = [[None if x == "." else x for x in y] for y in data]
    def get_adjacents(data, i, j):
        adjacents = []
        if i < 0 or i > len(data) or j < 0 or j > len(data[0]):
            return None
        if i == 0 and j == 0:
            adjacents.append(data[i + 1][j + 0])
            adjacents.append(data[i + 1][j + 1])
            adjacents.append(data[i + 0][j + 1])
        elif i == len(data) - 1 and j == len(data) - 1:
            adjacents.append(data[i - 1][j - 0])
            adjacents.append(data[i - 1][j - 1])
            adjacents.append(data[i - 0][j - 1])
        elif i == 0:
            adjacents.append(data[i + 1][j + 0])
            adjacents.append(data[i + 1][j + 1])
            adjacents.append(data[i + 0][j + 1])
            adjacents.append(data[i + 1][j - 1])
            adjacents.append(data[i + 0][j - 1])
        elif j == 0:
            adjacents.append(data[i + 0][j + 1])
            adjacents.append(data[i + 1][j + 1])
            adjacents.append(data[i + 1][j + 0])
            adjacents.append(data[i - 1][j + 1])
            adjacents.append(data[i - 1][j + 0])
        elif i == len(data) - 1:
            adjacents.append(data[i - 1][j + 0])
            adjacents.append(data[i - 1][j + 1])
            adjacents.append(data[i - 0][j + 1])
            adjacents.append(data[i - 1][j - 1])
            adjacents.append(data[i - 0][j - 1])
        elif j == len(data) - 1:
            adjacents.append(data[i + 0][j - 1])
            adjacents.append(data[i + 1][j - 1])
            adjacents.append(data[i + 1][j - 0])
            adjacents.append(data[i - 1][j - 1])
            adjacents.append(data[i - 1][j - 0])
        else:
            adjacents.append(data[i + 1][j + 0])
            adjacents.append(data[i + 1][j + 1])
            adjacents.append(data[i + 0][j + 1])
            adjacents.append(data[i + 1][j - 1])
            adjacents.append(data[i + 0][j - 1])
            adjacents.append(data[i - 1][j + 0])
            adjacents.append(data[i - 1][j + 1])
            adjacents.append(data[i - 1][j - 1])


    return

def solve_p2(data, *args, **kwargs):

    return

print(solve_p1("data/day_3.txt"))
print(solve_p2("data/day_3.txt"))