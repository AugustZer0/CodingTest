n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    x, y, z = map(int, input().split())

    # 제일 중요!
    z %= n

    # 좌측 회전
    if y == 0:
        arr[x-1] = arr[x-1][z:] + arr[x-1][:z]

    # 우측 회전
    if y == 1:
        arr[x-1] = arr[x-1][-z:] + arr[x-1][:-z]

total = 0
start, end = 0, n
for a in range(n):
    for b in range(start, end):
        total += arr[a][b]
    if a < (n // 2):
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(total)