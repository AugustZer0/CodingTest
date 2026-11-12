from collections import deque
t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = sorted(map(int, input().split()))
    queue = deque(arr)
    result = []

    while arr:
        if len(result) == 10:
            break

        else:
            a = queue.pop()
            result.append(a)
            b = queue.popleft()
            result.append(b)

    print(f"#{test_case}", *result)