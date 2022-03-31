'''
백트래킹 기본
'''

def permutation(i, p):
    # 원하는 숫자 개수에 도달했으면
    if i == M:
        print(' '.join(p))
    else:
        for j in range(1, N + 1):
            # 숫자 1부터 N까지 번갈아가면서 i번째 자리에 넣어줌
            if v[j] == 0:
                v[j] = 1
                p.append(str(j))
                permutation(i+1, p)
                
                # 복구(안 하면 원소가 그대로 p에 남아있고 v[j]도 계속 1이어서 중복이 되거나 사용을 못할 수 있음)
                p.pop()
                v[j] = 0

N, M = map(int, input().split())
v = [0] * (N + 1)
permutation(0, [])