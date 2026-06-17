n = int(input())

for i in range(n):
    txt = input().lower()
    if txt == txt[::-1]:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")