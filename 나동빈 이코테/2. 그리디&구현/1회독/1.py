n = int(input())

arr = [500, 100, 50, 10]
count = 0

for i in arr:
    count += n // i
    n %= i

print(count)