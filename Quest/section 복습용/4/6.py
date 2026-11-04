n = int(input())
arr = []
cnt = 0

for _ in range(n):
    h, w = map(int, input().split())
    arr.append((h, w))

arr.sort(reverse=True)

largest = 0

for h, w in arr:
    if w > largest:
        largest = w
        cnt += 1

print(cnt)