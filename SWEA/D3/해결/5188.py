def DFS(x, y, s):
    global res

    if s >= res:
        return

    if x == n - 1 and y == n - 1:
        if s < res:
            res = s
    else:
        if x < n - 1 and y < n - 1:
            DFS(x + 1, y, s + arr[x + 1][y])
            DFS(x, y + 1, s + arr[x][y + 1])
        elif x == n - 1:
            DFS(x, y + 1, s + arr[x][y + 1])
        elif y == n - 1:
            DFS(x + 1, y, s + arr[x + 1][y])
t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')
    DFS(0, 0, arr[0][0])
    print(f"#{test_case} {res}")