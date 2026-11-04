n = int(input())
arr = list(map(int, input().split()))
total = 0
cur = 0

for i in arr:
    if i == 1:
        cur += 1
        total += cur
    else:
        cur = 0

print(total)