# 다이나믹 프로그래밍
# 2부터 시작하기 때문에 현재 수보다 작은 수의 인덱스들은 모두 채워져있을 것
# -1한 수, 3으로 나눈 수, 2로 나눈 수들의 횟수 + 1이 현재 수의 횟수가 되므로
# 이들 중 가장 작은 것을 현재 횟수로 저장하면 됨
def makeOne(num):
    cnt = [0] * (num + 1)           # 인덱스가 num까지 있어야 함 
    for i in range(2, num + 1):     # 0, 1은 모두 0번
        c1 = c2 = c3 = 987654321    # NameError방지, 3으로 나눠지지 않는다면 c1은 없기 때문에
        if i % 3 == 0:
            c1 = cnt[i//3] + 1
        if i % 2 == 0:
            c2 = cnt[i//2] + 1
        c3 = cnt[i-1] + 1
        cnt[i] = min(c1, c2, c3)

    return cnt[num]


N = int(input())
rlt = makeOne(N)
print(rlt)