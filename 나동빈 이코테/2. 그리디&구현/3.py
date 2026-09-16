n = int(input())

x = list(map(int, input().split()))
x.sort()

count = 0
result = 0

for i in x:
    count += 1
    if count >= i:
        count = 0
        result += 1

print(result)