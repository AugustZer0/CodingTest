text = input()
stack = []

cnt = 0

for i in range(len(text)):
    if text[i] == "(":
        stack.append(text[i])
    else:
        stack.pop()
        if text[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)