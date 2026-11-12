t = int(input())
encrypt = ['0001101', '0011001', '0010011', '0111101', '0100011',
           '0110001', '0101111', '0111011', '0110111', '0001011']

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    code = ''
    for row in arr:
        if '1' in row:
            code = row.rstrip('0')[-56:]
            break

    pw = [encrypt.index(code[i:i+7]) for i in range(0, 56, 7)]
    ch = sum(pw[0::2]) * 3 + sum(pw[1::2])

    print(f"#{test_case} {sum(pw) if ch % 10 == 0 else 0}")