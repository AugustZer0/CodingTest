n, m = map(int, input().split())
arr = [0] * (n + m + 1)

for x in range(1, n + 1):
    for y in range(1, m + 1):
       arr[x + y] += 1

maxx = max(arr)

for i in range(n + m + 1):
    if arr[i] == maxx:
        print(i, end=' ')