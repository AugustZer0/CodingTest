t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    ch = [0] * (total + 1)
    ch[0] = 1

    for x in arr:
        for s in range(total -x, -1, -1):
            if ch[s]:
                ch[s + x] = 1

    print(f"#{test_case} {sum(ch)}")


""" DFS 시간 초과
def DFS(L, s):
    if L == n:
        score.add(s)
        return
    else:
        DFS(L + 1, s + arr[L])
        DFS(L + 1, s)

t = int(input())

# Test Case
for test_case in range(1, t + 1):

    n = int(input())
    arr = list(map(int, input().split()))
    score = set()
    DFS(0, 0)
    print(f"#{test_case} {len(score)}")
"""