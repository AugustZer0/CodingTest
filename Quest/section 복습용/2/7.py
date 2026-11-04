n = int(input())
arr = [0] * (n + 1)
cnt = 0

for x in range(2, n + 1):
    if arr[x] == 0:
        cnt += 1
        for y in range(x, n + 1, x):
            arr[y] = 1

print(cnt)