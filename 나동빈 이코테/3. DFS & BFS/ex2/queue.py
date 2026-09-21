from collections import deque

queue = deque()

while True:
    data = input()

    if data == "Q":
        print("종료 합니다")
        break
    elif data == "P":
        if not queue:
            print("큐에 아무것도 올라와있지 않습니다.")
        else:
            print(f"빠진 숫자; {queue[0]}")
            queue.popleft()
            print(f"현재 큐 상황 {queue}")
    else:
        queue.append(data)
        print(f"큐에 들어간 숫자: {data}")
        print(f"현재 큐 상황 {queue}")
