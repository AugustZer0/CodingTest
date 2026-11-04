from collections import deque

n, m = map(int, input().split())
arr = deque(sorted(list(map(int, input().split()))))
cnt = 0

while arr:
    if len(arr) == 1:
        cnt += 1
        break
    if arr[0] + arr[-1] <= m:
        arr.pop()
        arr.popleft()
        cnt += 1
    else:
        arr.pop()
        cnt += 1

print(cnt)