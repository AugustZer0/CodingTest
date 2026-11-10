# 5단계일 때, 칼로리를 안넘는 최고의 점수 제공
def DFS(L, s, k):
    global res
    if L == n:
        if k <= l:
            if s > res:
                res = s


    else:
        DFS(L + 1, s + score_arr[L], k + kcal_arr[L])
        DFS(L + 1, s, k)

# Test Case 수
t = int(input())

for i in range(1, t + 1):
    # 재료 갯수와 칼로리 제한
    n, l = map(int, input().split())
    score_arr = []
    kcal_arr = []
    res = -float('inf')
    for j in range(n):
        # 맛 점수와 칼로리 점수
        score, kcal = map(int, input().split())
        score_arr.append(score)
        kcal_arr.append(kcal)
    DFS(0, 0, 0)
    print(f"#{i} {res}")
