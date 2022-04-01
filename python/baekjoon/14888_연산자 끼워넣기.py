# 연산자는 +, -, *, / 순서


# 최소 구하는 함수
def findMin(i, s):
    global min_rlt, op_nums
    if i == N:
        if min_rlt > s:
            min_rlt = s

    # 가지치기할 때 조건 주의할 것!!!! s >= min_rlt가 앞에 있어야 함
    # 왜냐하면 뒤 조건은 s가 최소보다 더 클 때 뒤의 조건들이 있으면 더 작아질 수 없기 때문
    # 뒤 조건들이 앞으로 나오면 s가 최소보다 작은데도 그냥 -나 /가 없어서 리턴됨
    # 따라서 더 작아질 수도 있는데 막아버림
    # 최대도 마찬가지 and는 앞의 조건이 False면 뒤는 보지도 않기 때문에 이런 조건을 쓸 때는
    # 무조건!!! 가장 먼저 체크할 조건이 앞에 와야함
    # 나눗셈 연산자는 s가 양수여야 하는 이유는 음수는 나누면 더 커지기 때문
    elif s >= min_rlt and op_nums[1] == 0 and (s > 0 and op_nums[3] == 0):
        return

    else:
        for j in range(4):
            if op_nums[j]:
                op_nums[j] -= 1

                if j == 0:
                    findMin(i+1, s+nums[i])
                elif j == 1:
                    findMin(i+1, s-nums[i])
                elif j == 2:
                    findMin(i+1, s*nums[i])
                else:
                    if s < 0:
                        findMin(i+1, -((-s)//nums[i]))
                    else:
                        findMin(i+1, s//nums[i])

                op_nums[j] += 1


# 최대 구하는 함수
def findMax(i, s):
    global max_rlt, op_nums
    if i == N:
        if max_rlt < s:
            max_rlt = s

    # 가지치기
    # 음수는 곱하면 더 작아지기 때문에 s가 양수일 때만 곱셈 연산자의 유무를 봄
    elif s <= max_rlt and op_nums[0] == 0 and (s > 0 and op_nums[2] == 0):
        return

    # 연산자를 돌아가면서 써줌(연산자로 순열 만들기)
    else:
        for j in range(4):
            # i번째 수와 i + 1번째 수 사이의 연산을 정함
            if op_nums[j]:
                op_nums[j] -= 1

                if j == 0:
                    findMax(i+1, s+nums[i])
                elif j == 1:
                    findMax(i+1, s-nums[i])
                elif j == 2:
                    findMax(i+1, s*nums[i])
                else:
                    # 음수를 나눌 때는 양수로 바꾸고 몫을 취한 다음 음수로 바꾼다고 조건에 나옴
                    if s < 0:
                        findMax(i+1, -((-s)//nums[i]))
                    else:
                        findMax(i+1, s//nums[i])

                op_nums[j] += 1


N = int(input())
nums = list(map(int, input().split()))
op_nums = list(map(int, input().split()))
min_rlt = 1000011111
max_rlt = -1000011111

findMin(1, nums[0])
findMax(1, nums[0])

print(max_rlt)
print(min_rlt)