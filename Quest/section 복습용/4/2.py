def Count(length):
    cnt = 0
    for x in arr:
        cnt += x // length
    return cnt

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

lt = 0
rt = max(arr)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)