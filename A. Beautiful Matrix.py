a = []
for _ in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            x = [i, j]
            break
print(abs(x[0] - 2) + abs(x[1] - 2))
