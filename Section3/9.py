n = int(input())
result = []

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2]:
        result.append(10000 + a[0] * 1000)
    elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        result.append(max(a[0], a[1], a[2]) * 100)
    else:
        if a[0] == a[1]:
            result.append(1000 + a[0] * 100)
        elif a[1] == a[2]:
            result.append(1000 + a[1] * 100)
        elif a[2] == a[0]:
            result.append(1000 + a[2] * 100)


print(max(result))