# 회문인지 확인하는 함수
def isPal(n):
    length  = len(n)
    for i in range(length//2):
        if n[i] != n[length-1-i]:
            return 'NO'
    
    return 'YES'

T = int(input())

for _ in range(T):
    number = input()
    reverse_num = ''

    for i in range(len(number)-1, -1, -1):
        reverse_num += number[i]

    new_num = str(int(number)+int(reverse_num))

    rlt = isPal(new_num)

    print(rlt)
