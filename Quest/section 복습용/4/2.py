def Count(len):
    cnt = 0
    for x in arr:
        cnt += x // len
    return cnt

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

lt = 0
rt = max(arr)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1
print(res)