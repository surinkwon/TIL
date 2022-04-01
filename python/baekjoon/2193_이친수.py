def dp(num):
    lst = [0] * (num + 1)
    # 이렇게 지정해주기때문에 num이 1이면 인덱스 에러난다
    lst[1] = lst[2] = 1

    for i in range(3, num+1):
        # 범위 주의!!! num-1 까지라 하면 안 됨
        for j in range(1, i - 1):
            lst[i] += lst[j]
        lst[i] += 1

    return lst[num]

N = int(input())
if N != 1:
    print(dp(N))
else:
    print(1)
