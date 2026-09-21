n = int(input())

arr = list(map(int, input().split()))
arr.sort()

count = 0
result = 0
# 1 2 2 2 3
for i in arr:
    count += 1
    if count >= i:
        count = 0
        result += 1

print(result)