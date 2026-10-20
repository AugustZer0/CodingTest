n = int(input())
d1 = dict()

for _ in range(n):
    word = input()
    d1[word] = 1

for _ in range(n - 1):
    word = input()
    d1[word] -= 1

for key, val in d1.items():
    if val == 1:
        print(key)
        break