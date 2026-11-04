from collections import deque

n = int(input())
arr = deque(list(map(int, input().split())))
last = 0
result = ''

while True:
    candidates = []

    if len(arr) == 0:
        break

    if arr[0] > last:
        candidates.append((arr[0], "L"))
    if arr[-1] > last:
        candidates.append((arr[-1], "R"))

    if not candidates:
        break

    candidates.sort()
    last, d = candidates[0][0], candidates[0][1]

    if d == "L":
        result += "L"
        arr.popleft()

    elif d == "R":
        result += "R"
        arr.pop()


print(len(result))
print(result)
