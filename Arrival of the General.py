n = int(input())
a = list(map(int, input().split()))

max_index = a.index(max(a))
min_index = n - 1 - a[::-1].index(min(a))

moves = max_index + (n - 1 - min_index)

if min_index < max_index:
    moves -= 1

print(moves)
