from collections import deque

n = int(input())
arr = deque(list(map(int, input().split())))

last = 0
result = ""

while arr:
    l, r = arr[0], arr[-1]
    candidates = []

    if l > last:
        candidates.append((l, "L"))
    if r > last:
        candidates.append((r, "R"))

    if not candidates:
        break

    candidates.sort()

    last, d = candidates[0]
    if d == "L":
        arr.popleft()
        result += "L"
    if d == "R":
        arr.pop()
        result += "R"

print(len(result))
print(result)