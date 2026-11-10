table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
val = {ch: i for i, ch in enumerate(table)}

t = int(input())
for tc in range(1, t + 1):
    s = input().strip()
    res = []
    for i in range(0, len(s), 4):
        a, b, c, d = (val[ch] for ch in s[i:i + 4])
        bits = (a << 18) | (b << 12) | (c << 6) | d
        res.append(chr(bits >> 16))
        res.append(chr((bits >> 8) & 255))
        res.append(chr(bits & 255))
    print(f'#{tc} {"".join(res)}')