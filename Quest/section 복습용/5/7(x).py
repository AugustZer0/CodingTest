from collections import deque
s = input()
n = int(input())

for i in range(n):
    q = deque(s)
    plan = input()
    for x in plan:
        if x in q:
            if x != q.popleft():
                print(f"#{i + 1} NO")
                break

    else:
        if len(q) == 0:
            print(f"#{i + 1} YES")
        else:
            print(f"#{i + 1} NO")