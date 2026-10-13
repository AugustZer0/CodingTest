text = input()
res = ""
cnt = 0

for i in text:
    if i.isdigit():
        res += i
res = int(res)
print(res)

for x in range(1, int(res ** 0.5) + 1):
    if res % x == 0:
        if x * x == res:
            cnt += 1
        else:
            cnt += 2
print(cnt)
