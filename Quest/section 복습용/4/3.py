def Count(capacity):
    total = 0
    cnt = 1
    for x in arr:
        if total + x > capacity:
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
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)