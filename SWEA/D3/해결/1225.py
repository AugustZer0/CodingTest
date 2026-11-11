from collections import deque

for _ in range(10):
    test_case = int(input())
    arr = list(map(int, input().split()))
    queue = deque(arr)

    while queue[-1] > 0:
        for i in range(1, 6):
            v = queue.popleft()
            if (v - i) <= 0:
                queue.append(0)
                print(f"#{test_case}", *queue)
                break
            else:
                queue.append(v - i)