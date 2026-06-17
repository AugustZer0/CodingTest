n = [list(map(int, input().split())) for _ in range(7)]

count = 0

# 가로 방향으로 조사
for i in range(7):
    for j in range(3):
        if n[i][j] == n[i][j+4]:
            if n[i][j+1] == n[i][j+3]:
                count += 1

# 세로 방향으로 조사
for i in range(3):
    for j in range(7):
        if n[i][j] == n[i+4][j]:
            if n[i+1][j] == n[i+3][j]:
                count += 1


print(count)