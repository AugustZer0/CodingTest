t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    p = dict()
    cnt = 0

    for _ in range(n):
        word = input()
        if word in p:
            p[word] += 1
        else:
            p[word] = 1

    for _ in range(m):
        word = input()
        if word in p:
            p[word] += 1
        else:
            p[word] = 1

    for k, v in p.items():
        if v == 2:
            cnt += 1

    print(f"#{test_case} {cnt}")

