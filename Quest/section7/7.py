from collections import deque
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    cur = dQ.popleft()
    if cur == m:
        break
    for next in(cur - 1, cur + 1, cur + 5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[cur] + 1
print(dis[m])
