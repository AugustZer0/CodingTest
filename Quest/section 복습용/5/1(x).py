n, m = map(int, input().split())
n = list(map(int, str(n)))

# FILO(선입후출)
stack = []

for i in n:
    while stack and m > 0 and i > stack[-1]:
        stack.pop()
        m -= 1
    stack.append(i)

# m이 남으면 뒤에거 잘라냄
if m!= 0:
    stack = stack[:-m]

for j in stack:
    print(j, end='')