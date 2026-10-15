n, m = map(int, input().split())
arr = list(map(int, input().split()))


lt = 0
rt = 1
total = arr[lt]
cnt = 0

while True:
    if total < m:
        if rt < n:
            total += arr[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= arr[lt]
        lt += 1
    else:
        total -= arr[lt]
        lt += 1

print(cnt)