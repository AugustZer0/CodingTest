n = int(input())

arr = []
for _ in range(n):
    height, weight = map(int, input().split())
    arr.append((height, weight))
arr.sort(reverse=True)

largest = 0
cnt = 0

for h, w in arr:
    if w > largest:
        cnt += 1
        largest = w

print(cnt)