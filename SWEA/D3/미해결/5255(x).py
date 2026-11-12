dp = [0] * 31
dp[0], dp[1], dp[2] = 1, 1, 3
for i in range(3, 31):
    dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3]

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    print(f"#{test_case} {dp[n]}")