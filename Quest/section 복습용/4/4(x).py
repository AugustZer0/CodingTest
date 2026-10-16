def Count(len):
    cnt = 1
    ep = arr[0]
    for i in arr:
        if i - ep >= len:
            cnt += 1
            ep = i
    return cnt

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

# 거리에 대해 lt(떨어질 수 있는 최소 거리), rt(최대 거리)를 잡아야함
lt = 1
rt = arr[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
