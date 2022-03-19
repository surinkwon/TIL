from collections import deque

M = input()
stack = deque()
num = ''

for i in range(len(M)):
    if M[i] != '+' and M[i] != '-':
        num += M[i]
    else:
        stack.append(int(num))
        stack.append(M[i])
        num = ''
stack.append(int(num))

stack2 = deque()
stack2.append(stack[0])
i = 1
while i < len(stack) - 1:
    number = 0
    if stack[i] != '+' and stack[i+1] != '+':
        stack2.append(stack[i])
        i += 1
    else:
        if stack[i] == '+':
            i +=1

        number += stack[i]
        i += 2
        while i < len(stack) and stack[i-1] != '-':
            number += stack[i]
            i += 2
        stack2.append(number)
        i -= 1

if i == len(stack) - 1:
    stack2.append(stack[len(stack)-1])

rlt = stack2[0]

for i in range(len(stack2) - 1, 0, -2):
    if stack2[i - 1] == '-':
        rlt -= stack2[i]
    else:
        rlt += stack2[i]

print(rlt)
