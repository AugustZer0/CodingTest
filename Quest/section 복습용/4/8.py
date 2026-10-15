from collections import deque
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

arr = deque(arr)
cnt = 0

while arr:
    if len(arr) == 1:
        cnt += 1
        break
    if arr[0] + arr[-1] > m:
        arr.pop()
        cnt += 1
    else:
        arr.popleft()
        arr.pop()
        cnt += 1

print(cnt)