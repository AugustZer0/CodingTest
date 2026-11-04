n = int(input())

for i in range(n):
    text = input().lower()
    if text == text[::-1]:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")