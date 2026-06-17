n, m = map(int, input().split())

a = list(map(int, input().split()))

lt = 0
rt = 1

count = 0
tot = a[0]

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        count += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
    
    
print(count)
            