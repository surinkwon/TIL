import sys
def insf(s):
    stack = [0] * (len(s) + 1)
    top = -1

    for i in range(len(s)):
        # 여는 괄호면 스택에 저장
        if s[i] == '(' or s[i] == '[':
            top += 1
            stack[top] = s[i]

        # 닫는 괄호면 짝이 맞지 않으면 no 반환
        elif s[i] == ')':
            if top < 0 or stack[top] != '(':
                return 'no'
            else:
                top -= 1

        elif s[i] == ']':
            if top < 0 or stack[top] != '[':
                return 'no'
            else:
                top -= 1

    # 여는 괄호가 남아있으면 짝이 맞지 않으므로 no 반환
    if top < 0 :
        return 'yes'
    else:
        return 'no'


while True:
    string = sys.stdin.readline().strip('\n')

    if string == '.':
        break
    else:
        rlt = insf(string)
        print(rlt)
