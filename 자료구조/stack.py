stack = []

while True:
    data = input()

    if data == "Q":
        break
    elif data == "P":
        if not stack:
            print("스택에 아무것도 없습니다.")
        print(f"pop한 숫자: {stack.pop()}")
    else:
        stack.append(data)
        print(f"stack 현황 {stack}")