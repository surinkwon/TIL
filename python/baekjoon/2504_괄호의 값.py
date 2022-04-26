'''
stack
'''
def howMuchValue(s):
    stack = []
    v = 1
    total_v = 0
    for i in range(len(s)):
        # 닫는 괄호일 때만 계산해주면 되므로 여는 괄호일 때는 값에 해당 값만큼 곱해줌
        if s[i] == '(' or s[i] == '[':
            if s[i] == '(':
                stack.append('(')
                v *= 2
            else:
                stack.append('[')
                v *= 3
        else:
            # 닫는 괄호인데 앞에 여는 괄호가 없거나
            if not stack:
                return 0
            # 서로 다른 짝이면
            elif (stack[len(stack)-1] == '(' and s[i] == ']') or (stack[len(stack)-1] == '[' and s[i] == ')'):
                return 0
            else:
                # 짝이 다 맞으면
                stack.pop()
                
                # 값을 최종 값에 더해주고
                if i == len(s) - 1 or s[i+1] == '(' or s[i+1] == '[':
                    total_v += v
                    j = i
                    # 여태까지 지나온 닫는괄호만큼 값을 나눠줌
                    while s[j] != '[' and s[j] != '(':
                        if s[j] == ']':
                            v //= 3
                        else:
                            v //= 2
                        j -= 1
    
    # 문자열을 다 돌았는데 스택에 괄호가 남아있으면 짝이 안 맞는다는 뜻
    if stack:
        return 0

    return total_v


string = list(input())
total = howMuchValue(string)
print(total)
