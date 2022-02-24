import sys

sys.stdin = open('input.txt')

T = 10

# 후위표기 함수
def postfix(fomul):
    # 결과와 연산자를 따로 저장하기 위해 각각 리스트, 스택 생성
    rlt_lst = [0] * len(fomul)
    op_stack = [0] * len(fomul)
    rlt_top = op_top = -1

    for i in range(len(fomul)):
        # 수식에서의 값이 숫자일 때
        if fomul[i] != '+' and fomul[i] != '*':
            rlt_top += 1
            rlt_lst[rlt_top] = fomul[i]
            
        # 값이 연산자일 때
        else:
            # 맨 처음에는 연산자를 push해줌
            if op_top == -1:
                op_top += 1
                op_stack[op_top] = fomul[i]
            else:
                # 수식의 값과 연산자 스택 top의 값이 같으면 같은 값을 pop 하고 push하므로
                # 결과 스택에 해당 값을 저장해주기만 하면 됨
                if fomul[i] == op_stack[op_top]:
                    rlt_top += 1
                    rlt_lst[rlt_top] = fomul[i]

                else:
                    # fomul의 값이 +인데 op의 값은 *일 때는
                    # op_stack의 값이 +가 아닐 때까지 pop
                    if fomul[i] == '+' and op_stack[op_top] == '*':
                        while op_stack[op_top] != '+' and op_top > -1:
                            rlt_top += 1
                            rlt_lst[rlt_top] = op_stack[op_top]
                            op_top -= 1
                        
                        # *연산이 나오기 전에 +연산이 하나도 없었다면 +를 다시 push해줘야 함 
                        if op_top == -1:
                            op_top += 1
                            op_stack[op_top] = fomul[i]
                        # +연산이 하나라도 있었다면 pop과 push를 동시에 하므로 결과 스택에만 추가해주면 됨
                        else:
                            rlt_top += 1
                            rlt_lst[rlt_top] = fomul[i]

                    # fomul의 값이 *인데 op의 값은 +일 때는 
                    # op_stack에 push해줌
                    elif fomul[i] == '*' and op_stack[op_top] == '+':
                        op_top += 1
                        op_stack[op_top] = fomul[i]

    # 연산자 스택에 남아있는 값이 없을 때까지 결과스택에 push
    while op_top != -1:
        rlt_top += 1
        rlt_lst[rlt_top] = op_stack[op_top]
        op_top -= 1

    return rlt_lst

# 계산 함수
def cal(fomul):
    stack = [0] * len(fomul)
    top = -1
    # 수식을 앞에서부터 읽어가면서 계산
    for i in range(len(fomul)):
        # 읽어온 값이 숫자라면 스택에 push
        if fomul[i] != '*' and fomul[i] != '+':
            top += 1
            stack[top] = int(fomul[i])
        else:
            # 연산자라면 top과 top - 1에 있는 값을 해당 연산자로 처리해줌
            if fomul[i] == '+':
                top -= 1
                stack[top] = stack[top] + stack[top + 1]
            else:
                top -= 1
                stack[top] = stack[top] * stack[top + 1]

    return stack[0]

for tc in range(1, T + 1):
    num = int(input())
    word = input()
    rlt = cal(postfix(word))
    print(f'#{tc} {rlt}')

