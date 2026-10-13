n = int(input())
arr = list(map(int, input().split()))

current = 0
result = 0

for i in arr:
    if i == 1:
        current += 1
    else:
        current = 0
    result += current

print(result)