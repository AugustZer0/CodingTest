stack = []

while True:
    data = input()

    if data == "Q":
        print("종료 합니다")
        break
    elif data == "P":
        if not stack:
            print("아무것도 없습니다.")
        else:
            print(f"빠진 숫자: {stack[-1]}")
            stack.pop()
            print(f"현재 스택 상황 {stack}")
    else:
        stack.append(data)
        print(f"추가된 숫자{data}")
        print(f"현재 스택 상황 {stack}")
