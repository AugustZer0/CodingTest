def digit_sum(x):
    return sum(int(i) for i in x)

if __name__ == "__main__":
    n = int(input())
    arr = list(input().split())
    tmp = 0

    for k, v in enumerate(arr):
        s = digit_sum(v)
        if tmp < s:
            tmp = s
            i = k
    print(arr[i])
