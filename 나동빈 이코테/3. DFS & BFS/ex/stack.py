stack = []

while True:
    data = input()

    if data == "Q":
        break

    elif data == "P":
        if not stack:
            print("아무것도 없습니다.")
        else:
            stack.pop()
            print(stack)
    else:
        stack.append(data)
        print(stack)
