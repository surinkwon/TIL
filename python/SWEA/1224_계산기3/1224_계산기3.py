import sys

sys.stdin = open('input.txt')

T = 10

operator = ['+', '*', '(', ')']

# 후위 표기식 구하는 함수
def postFix(fomul):
    rlt = [0] * len(fomul)
    op = [0] * len(fomul)
    rlt_t = op_t = -1

    for i in range(len(fomul)):
        # 숫자면 결과에 푸시
        if fomul[i] not in operator:
            rlt_t += 1
            rlt[rlt_t] = fomul[i]
        # 연산자면
        else:
            if op_t == -1: # 스택이 비었으면 무조건 푸시해줌
                op_t += 1
                op[op_t] = fomul[i]
            else:
                # 여는 괄호면 연산자 스택에 push
                if fomul[i] == '(' or op[op_t] == '(':
                    op_t += 1
                    op[op_t] = fomul[i]

                # 닫는 괄호면 여는 괄호가 나올때까지 pop
                elif fomul[i] == ')':
                    while op[op_t] != '(':
                        rlt_t += 1
                        rlt[rlt_t] = op[op_t]
                        op_t -= 1
                    op_t -= 1 # '('를 버려줌

                # 닫는 괄호가 나오기 전까지는 일반 식과 동일하게 push 혹은 pop
                else:
                    # 수식과 연산자 스택의 값이 같으면 결과에 push
                    if fomul[i] == op[op_t]:
                        rlt_t += 1
                        rlt[rlt_t] = fomul[i]
                    # 수식은 +, 연산자 스택은 *이면
                    elif fomul[i] == '+' and op[op_t] == '*':
                        # 여는 괄호가 앞에 있으면 스택의 시작과 동일하게 취급
                        # 스택의 시작점이 아니면 *을 먼저 결과에 push하고 그 다음 +를 push
                        if op_t != 0 and op[op_t - 1] != '(':
                            rlt_t += 2
                            rlt[rlt_t - 1] = op[op_t]
                            rlt[rlt_t] = op[op_t - 1]
                            op_t -= 1
                        # 스택의 시작점이라면 결과에 * push하고 연산자 스택 top을 +로 바꿔줌
                        else:
                            rlt_t += 1
                            rlt[rlt_t] = op[op_t]
                            op[op_t] = fomul[i]
                    
                    # 수식이 * 연산자 스택이 +이거나, 연산자 스택이 (일 때는 그냥 연산자 스택에 push 해줌
                    else:
                        op_t += 1
                        op[op_t] = fomul[i]
    return rlt


# 계산 함수
def cal(post_fomul):
    stack = [0] * len(post_fomul)
    top = -1

    # 후위표기식을 앞에서부터 읽어가며 계산
    for i in range(len(post_fomul)):
        if post_fomul[i] not in operator:
            top += 1
            stack[top] = int(post_fomul[i])
        else:
            num2 = stack[top]
            num1 = stack[top - 1]
            top -= 1
            if post_fomul[i] == '+':
                stack[top] = num1 + num2
            else:
                stack[top] = num1 * num2

    return stack[0]


for tc in range(1, T + 1):
    N = int(input())
    fomul = input()

    post = postFix(fomul)
    rlt = cal(post)

    print(f'#{tc} {rlt}')

