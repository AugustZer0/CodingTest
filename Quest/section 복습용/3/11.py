arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 가로 줄
for i in range(7):
    for j in range(3):
        lines = arr[i][j:j+5]
        if lines == lines[::-1]:
            cnt += 1

# 세로 줄
for i in range(7):
    for j in range(3):
        lines = [arr[j+k][i] for k in range(5)]
        if lines == lines[::-1]:
            cnt += 1

print(cnt)