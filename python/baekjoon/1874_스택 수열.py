import sys

N = int(input())
op = []             # 연산자 순서 담을 배열
stack = [0] * N     # 수 담을 스택
stack[0] = 1        # 스택에 1을 항상 먼저 추가해 놓음
op.append('+')      # 추가 연산을 op에 추가
cn = 2              # 1의 다음 수부터 삽입하므로 현재 수는 2
top = 0             # 스택에 1을 삽입했으므로 현재 탑은 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if stack[top] == num:                   # 스택의 탑과 출력할 수열의 수가 같으면
        op.append('-')                      # pop하고 연산자 배열에 -추가
        top -= 1
    else:                                   # 스택의 탑과 출력할 수열의 수가 다르면
        if stack[top] > num:                # 스택의 탑이 출력할 수보다 크면 절대 해당 수열은 만들 수 없음
            continue
        else:                               # 그렇지 않으면
            for i in range(cn, num + 1):    # 해당 수 차례가 올 때까지 스택에 push
                top += 1
                stack[top] = cn
                cn += 1
                op.append('+')              # 연산자 배열에 +추가
            op.append('-')                  # 맨 마지막에는 탑에 해당 수가 오기 때문에 pop해줌
            top -= 1

# 만들 수 없는 수열이면 중간에 continue해주기 때문에 절대 top이 -1이 될 수 없음
if top > -1:
    print('NO')
else:
    for i in range(len(op)):
        print(op[i])