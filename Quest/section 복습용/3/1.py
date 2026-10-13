n = int(input())

for i in range(1, n + 1):
    text = input().lower()
    if text == text[::-1]:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")