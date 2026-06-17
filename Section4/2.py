n = input()

tmp = ""
count = 0

for x in n:
    if x.isdecimal():
        tmp += x

tmp = int(tmp)

for i in range(1, tmp + 1):
    if tmp % i == 0:
        count += 1

print(tmp)
print(count)