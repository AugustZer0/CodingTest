t = int(input())

for test_case in range(1, t + 1):
    n, s = input().split()
    n = int(n)
    arr = set()

    # 몇 글자씩 떼갈지 설정 (1 ~ 최대 글자수)
    for i in range(1, len(s) + 1):
        # 어디서부터 떼갈지 설정 (0 ~ 최대 글자수 - 1)
        for j in range(len(s)):
            if i + j > len(s):
                break
            else:
                arr.add(s[j:j + i])

        if len(arr) > 2 * n:
            arr = set(sorted(arr)[:n])

    arr = sorted(arr)
    print(f"#{test_case} {arr[n - 1][0]} {len(arr[n-1])}")