n, k = map(int, input().split())
arr = list(map(int, input().split()))
total = []
for x in range(n - 2):
    for y in range(x + 1, n - 1):
        for z in range(y + 1, n):
            total.append(arr[x] + arr[y] + arr[z])

total = sorted(list(set(total)), reverse=True)
print(total[k - 1])