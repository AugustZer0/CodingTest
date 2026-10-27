n, m = map(int, input().split())
g=[[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()

"""
n, m = map(int, input().split())

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    start, goal, value = map(int, input().split())
    result[start - 1][goal - 1] = value

for x in result:
    print(*x)
"""