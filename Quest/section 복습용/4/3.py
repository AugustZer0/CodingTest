def Count(capacity):
    cnt = 1
    total = 0
    for x in arr:
        if x + total > capacity:
            cnt += 1
            total = x
        else:
            total += x
    return cnt

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = max(arr)
rt = sum(arr)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1

print(res)
