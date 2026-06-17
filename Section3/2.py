# 테스트 케이스 수
t = int(input())

for i in range(1, t + 1):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    
    print(f"#{i} {a[k-1]}")