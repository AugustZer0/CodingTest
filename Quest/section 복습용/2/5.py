n, m = map(int, input().split())

a = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i + j] += 1

max_value = max(a)

for x,y in enumerate(a):
    if max_value == y:
        print(x, end=" ")

