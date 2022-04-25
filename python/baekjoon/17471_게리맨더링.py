'''
부분집합 구하는 것처럼 dfs 돌리고 두 부분집합이 나눠지면
각각 bfs를 돌려서 연결되어있는지 확인
연결되어있다면 인구수 계산

입력받을 때 연결되어 있는 번호가 1번부터 시작하기 때문에 여기에 맞춰서 작성해줘야함!!!
'''
from collections import deque

def isConnected(lst):
    q = deque()
    v = [0] * (N + 1)
    q.append(lst[0])
    v[lst[0]] = 1
    cnt = 1

    while q:
        cn = q.popleft()
        
        # 도시 수가 리스트 수와 같다면 모두 연결됐다는 것ㄴ
        if cnt == len(lst):
            return 1

        for d in range(len(cities[cn])):
            nn = cities[cn][d]
            # 도시가 구역에 있는 도시 리스트에 있고 방문하지 않았으면
            if nn in lst and v[nn] == 0:
                q.append(nn)
                v[nn] = 1
                cnt += 1
    
    return 0


def devide(i, a_p, b_p, a_s, b_s):
    global min_d

    # 둘로 나눴으면
    if i == N + 1:
        # 나눈 것에 도시가 하나라도 있어야 함(공집합이 있으면 안 됨)
        if a_p and b_p:
            # 두 구역 모두 각각 이어져있으면
            if isConnected(a_s) and isConnected(b_s):
                # 차이가 작으면 갱신
                if min_d > abs(a_p-b_p):
                    min_d = abs(a_p-b_p)
    else:
        a_s.append(i)
        devide(i+1, a_p+populations[i], b_p, a_s, b_s)
        a_s.pop()
        b_s.append(i)
        devide(i+1, a_p, b_p+populations[i], a_s, b_s)
        b_s.pop()


N = int(input())
populations = [0] + list(map(int, input().split()))
cities = [0] * (N + 1)
min_d = 987654321

# 연결된 도시 정보 받기
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    cities[i] = data[1:]

# 도시 둘로 나누고 인구 수 차이 구함
devide(1, 0, 0, [], [])

if min_d != 987654321:
    print(min_d)
else:
    print(-1)