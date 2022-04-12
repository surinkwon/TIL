'''
유클리드호제
'''

from cgitb import small


num1, num2 = map(int, input().split(':'))

if num1 == num2:
    print('1:1')
else:
    b = max(num1, num2)
    s = min(num1, num2)

    rest = b % s
    while rest != 0:
        b = s
        s = rest
        rest = b % s
    
    print(f'{num1//s}:{num2//s}')
