k, n = map(int, input().split())

a = [int(input()) for _ in range(k)]

lt = 1
rt = max(a)
answer = 0

def count(len):
    count = 0
    for x in a:
        count += (x // len)
    return count

while lt <= rt:
    mid = (lt + rt) // 2

    if count(mid) >= n:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)
