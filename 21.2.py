print("Транспонирование")


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)

print("____________")
matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)

input("Press any key to exit")
exit(0)
