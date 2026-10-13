def digit_sum(x):
    total = 0
    for i in x:
        total += int(i)
    return total

n = int(input())
arr = input().split()

max_value = 0

for x in arr:
    s = digit_sum(x)
    if s > max_value:
        max_value = s
        res = x

print(res)