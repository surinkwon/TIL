'''
1과 0 중 어떤 게 더 적게 띄어져있는지 확인하고 그 수 출력
'''

string = input()

i = cnt_one = cnt_zero = 0
num_one = num_zero = 0

while i < len(string):
    while i < len(string) and string[i] == '1':
        cnt_one += 1
        i += 1
    while i < len(string) and string[i] == '0':
        cnt_zero += 1
        i += 1
    
    if cnt_one:
        num_one += 1
        cnt_one = 0
    
    if cnt_zero:
        num_zero += 1
        cnt_zero = 0

print(min(num_one, num_zero))
