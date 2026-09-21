def recursive_fuction(i):
    if i == 100:
        return
    print(f"{i}번쨰 재귀함수를 호출합니다.")
    recursive_fuction(i + 1)
    print(f"{i}번째 재귀함수를 종료합니다.")

recursive_fuction(1)