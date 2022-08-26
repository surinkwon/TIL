'''
대진표가 주어지면 정해진 두 사람이 몇 번째 라운드에서 만나는지 구하는 문제
'''

def solution(n,a,b):
    # 1라운드부터 시작
    answer = 1
    
    for _ in range(n):
        if (a == b + 1 or b == a + 1) and (a // 2 != b // 2):
            return answer
        
        # 이겼을 때 다음 라운드에서 몇번인지 구함
        if a % 2:
            a = a // 2 + 1
        else:
            a //= 2
        
        if b % 2:
            b = b // 2 + 1
        else:
            b //= 2
        
        answer += 1