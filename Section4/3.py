n, m = map(int, input().split())

a = list(map(int, input().split()))

lt = max(a)
rt = sum(a)

result = 0

def count(capacity):
    total = 0
    count = 1

    for x in a:
        if total + x > capacity:
            count += 1
            total = x
        else:
            total += x

    return count

while lt <= rt:
    mid = (lt + rt) // 2
    
    if count(mid) <= m:
        result = mid
        rt = mid - 1
    else:
        lt = mid + 1


print(result)
