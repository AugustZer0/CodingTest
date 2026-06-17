n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

tmp = []

for i in a:
    tmp.append(sum(i))
    
for i in range(n):
    total = 0
    for j in range(n):
        total += a[j][i]
    tmp.append(total)
    
    
total = 0
for i in range(n):
    total += a[i][i]
tmp.append(total)

total = 0
for i in range(n - 1, -1, -1):
    total += a[i][n - 1 - i]
tmp.append(total)

print(max(tmp))
    