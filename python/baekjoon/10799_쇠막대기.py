'''
레이저를 쏘면 여태까지 쌓였던 막대기 수만큼 나눠짐
'''

data = input()

total_stick = cur_stick = 0

for i in range(len(data)):
    if data[i] == '(':
        if data[i + 1] != ')':
            cur_stick += 1
    else:
        if data[i - 1] == '(':
            total_stick += cur_stick
        else:
            total_stick += 1
            cur_stick -= 1

print(total_stick)