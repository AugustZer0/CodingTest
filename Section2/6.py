def digit_sum(x):
    res = 0
    for digit in x:
        res += int(digit)
    return res

n = int(input())
a = list(input().split())

max_sum = -1
ans = ""

for num in a:
    current_sum = digit_sum(num)
    
    if current_sum > max_sum:
        max_sum = current_sum
        ans = num

print(ans)

a = ["125", "15232", "97"]

for x in a:
    res = 0
    for digit in x:
        res += int(digit)
    print(res)