from collections import deque

n, k = map(int, input().split())
arr = deque([i + 1 for i in range(n)])

while arr:
    for _ in range(k - 1):
        cur = arr.popleft()
        arr.append(cur)
    arr.popleft()

    if len(arr) == 1:
        print(arr[0])
        arr.popleft()
