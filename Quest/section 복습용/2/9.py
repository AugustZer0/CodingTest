n = int(input())
res = 0

for _ in range(n):
    x, y, z = sorted(list(map(int, input().split())), reverse=True)
    if x == z:
        prize = 10000 + x * 1000
    elif y == x or y == z:
        prize = 1000 + y * 100
    else:
        prize = 100 * x

    res = max(res, prize)

print(res)