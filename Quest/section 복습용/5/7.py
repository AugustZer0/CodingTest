from collections import deque
s = input()
n = int(input())

for i in range(n):
    plan = input()
    queue = deque(s)
    for x in plan:
        if x in queue:
            if x != queue.popleft():
                print(f"#{i + 1} NO")
                break
    else:
        if len(queue) == 0:
            print(f"#{i + 1} YES")
        else:
            print(f"#{i + 1} NO")