def findPer(i, n, num_lst):
    global rlt, v

    if i == n:
        rlt.add(tuple(num_lst))

    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                num_lst.append(nums[j])
                findPer(i+1, n, num_lst)
                v[j] = 0
                num_lst.pop()

N, M = map(int, input().split())

nums = list(map(int, input().split()))

# 중복 방지를 위해 셋으로 처리
rlt = set()
v = [0] * N

findPer(0, M, [])

rlt = sorted(list(rlt))

# 맨 마지막 줄 아래에 공백 출력 방지
for i in range(len(rlt) - 1):
    for j in range(M):
        print(rlt[i][j], end=' ')
    print()

for i in range(M):
    print(rlt[-1][i], end=' ')