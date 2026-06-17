n = int(input())

a = list(map(int, input().split()))
score = 0
result = 0

for i in a:
    if i == 1:
        score += 1
        result += score
    else:
        score = 0

print(result)