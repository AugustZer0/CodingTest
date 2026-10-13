# 리스트 해쉬
a = input()
b = input()

str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper(): # 대문자는 65~90
        str1[ord(x) - 65] += 1
    else: # 소문자는 97~122 -> 97-71 = 26 소문자a를 26부터 시작할 예정
        str1[ord(x) - 71] += 1
for x in b:
    if x.isupper(): # 대문자는 65~90
        str1[ord(x) - 65] += 1
    else: # 소문자는 97~122 -> 97-71 = 26 소문자a를 26부터 시작할 예정
        str1[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")