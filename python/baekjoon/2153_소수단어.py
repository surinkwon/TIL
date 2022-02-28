# 소수인지 판별하는 함수
def primeNum(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    
    return 1


# 대소문자 나눠서 아스키코드로 숫자를 구함
word = input()
total = 0

for idx in range(len(word)):
    if 'a' <= word[idx] <= 'z':
        total += ord(word[idx]) - 96
    else:
        total += ord(word[idx]) - 38

rlt = primeNum(total)
if rlt:
    print('It is a prime word.')
else:
    print('It is not a prime word.')


