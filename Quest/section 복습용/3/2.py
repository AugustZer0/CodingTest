text = input()
result = ''
cnt = 0

for i in text:
    if i.isdigit():
        result += i

result = int(result)
print(result)

for i in range(1, int(result ** 0.5) + 1):
    if result % i == 0:
        if i * i == result:
            cnt += 1
        else:
            cnt += 2
print(cnt)