t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    x = y = d = 0
    for num in range(1, n * n + 1):
        arr[x][y] = num
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny]:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]
        x, y = nx, ny

    print(f"#{i}")
    for row in arr:
        print(*row)