from collections import deque

queue = deque()

while True:
    data = input()

    if data == 'q':
        break

    elif data == 'p':
        if not queue:
            print("아무 숫자도 없습니다.")
        print(f"pop한 숫자 {queue.popleft()}")

    else:
        queue.append(data)
        print(f"현재 Queue 상황 {queue}")