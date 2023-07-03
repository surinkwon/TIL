import sys

t = 1

while True:
    S = sys.stdin.readline()

    if S[0] == '-':
        break

    stack = []
    cnt = 0

    for i in range(len(S) - 1):
        if S[i] == '{':
            stack.append(S[i])
        elif len(stack) == 0 and S[i] == '}':
            cnt += 1
            stack.append('{')
        else:
            stack.pop()
    
    # 스택에는 여는 괄호만 남아있으므로 닫는 괄호와 짝을 맞춰주는 연산 필요
    cnt += len(stack) // 2

    print(f'{t}. {cnt}')
    t += 1