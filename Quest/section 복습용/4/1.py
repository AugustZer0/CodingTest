n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

lt = 0
rt = n

while True:
    mid = (lt + rt) // 2
    if arr[mid] < m:
        lt = mid + 1
    elif arr[mid] > m:
        rt = mid - 1
    else:
        print(mid + 1)
        break