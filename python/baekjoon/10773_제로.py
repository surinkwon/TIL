N = int(input())
stack = [0] * N
top = -1

for _ in range(N):
    num = int(input())
    if num:
        top += 1
        stack[top] = num
    else:
        stack[top] = 0
        top -= 1

print(sum(stack))
