def DFS():
    pass

t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
