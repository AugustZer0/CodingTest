from collections import deque

queue = deque()

while True:
    data = input()

    if data == "Q":
        break

    elif data == "P":
        if not queue:
            print("아무것도 없습니다.")
        else:
            queue.popleft()
            print(queue)

    else:
        queue.append(data)
        print(queue)