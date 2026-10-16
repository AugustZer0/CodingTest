# 개선 버전
a = input()
b = input()
s = dict()

for x in a:
    s[x] = s.get(x, 0) + 1

for x in b:
    s[x] = s.get(x, 0) - 1

for x in a:
    if s.get(x) > 0:
        print("NO")
        break
else:
    print("YES")