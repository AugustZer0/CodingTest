n = int(input())
arr = [500, 100, 50, 10]

coin = 0
for i in arr:
    coin += n // i
    n %= i

print(coin)