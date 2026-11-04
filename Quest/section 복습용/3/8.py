n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    x, y, z = map(int, input().split())
    z %= n
    if y == 0:
        arr[x - 1] = arr[x - 1][z:] + arr[x - 1][:z]
    elif y == 1:
        arr[x - 1] = arr[x - 1][-z:] + arr[x- 1][:-z]

s = 0
e = n
total = 0
for i in range(n):
    for j in range(s, e):
        total += arr[i][j]
    if i >= n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(total)