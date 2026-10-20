from collections import Counter

a = input()
b = input()

if Counter(a) == Counter(b):
    print("YES")
else:
    print("NO")