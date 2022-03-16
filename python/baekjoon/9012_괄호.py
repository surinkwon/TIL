# 스택으로 괄호 검사
from inspect import stack
import sys


def ins(list):
    top = -1
    for i in range(len(list) - 1):
        if list[i] == '(':
            top += 1
        else:
            if top > -1:
                top -= 1
            else:
                return 'NO' # 닫는 괄호가 들어왔는데 앞에 여는 괄호가 없을 경우
    
    if top == -1:
        return 'YES' # 닫는 괄호와 여는 괄호가 짝이 모두 맞을 때
    else:
        return 'NO' # 여는 괄호가 닫는 괄호보다 더 많을 때


N = int(input())

for _ in range(N):
    lst = list(sys.stdin.readline())
    rlt = ins(lst)
    
    print(rlt)
