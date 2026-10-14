arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
# x축 체크
for i in range(7):
    for j in range(3):
        if arr[i][j:j+5] == arr[i][j:j+5][::-1]:
            cnt += 1

# y축 체크
for i in range(3):
    for j in range(7):
        lines = [arr[i+k][j] for k in range(5)]
        if lines == lines[::-1]:
            cnt += 1
print(cnt)