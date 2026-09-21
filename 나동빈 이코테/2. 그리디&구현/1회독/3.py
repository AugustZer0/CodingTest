text = input()
result = int(text[0])

for i in text[1:]:
    num = int(i)
    if result <= 1 or int(i) <= 1:
        result += num
    else:
        result *= num

print(result)