t = int(input())

for test_case in range(1, t + 1):
    n = float(input())
    res = ""
    while n > 0 and len(res) < 13:
        n *= 2
        if n >= 1:
            res += '1'
            n -= 1
        else:
            res += '0'

    if n > 0 or len(res) > 12:
        print(f"#{test_case} overflow")
    else:
        print(f"#{test_case} {res}")