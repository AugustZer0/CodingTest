# 시간/공간 복잡도에서 가성비 + break 덕분에 답만 구하고 끝남
n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            break
else:
    print(-1)