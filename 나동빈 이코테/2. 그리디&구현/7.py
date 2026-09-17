data = input()

tmp = []
result = ""
value = 0

for i in data:
    if i.isalpha():
        tmp.append(i)
    else:
        value += int(i)

tmp.sort()

for j in tmp:
    result += j

result += str(value)
print(result)