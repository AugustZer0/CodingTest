from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n + 1)])

while arr:
    for i in range(k - 1):
        arr.append(arr.popleft())
    arr.popleft()
    if len(arr) == 1:
        print(arr[0])
        arr.popleft()