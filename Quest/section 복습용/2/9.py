n = int(input())
best = 0

for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    if a == b == c:
       prize = 10000 + a * 1000
    elif b == a or b == c:
        prize = 1000 + b * 100
    else:
        prize = 100 * c
    best = max(best, prize)

print(best)