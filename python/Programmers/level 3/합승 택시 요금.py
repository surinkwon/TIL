from collections import deque

# s에서 다른 지점들까지의 최소 경비 및 경로를 찾는 함수
def findWay(n, s, connection):
    q = deque()
    v = [[] for _ in range(n + 1)]
    q.append([0, s])
    v[s].append(0)

    while q:
        cv = q.popleft()
        cf, cn = cv[0], cv[-1]

        for d in range(len(connection[cn])):
            nn, f = connection[cn][d]

            if not v[nn] or v[nn][0] > cf + f:
                tmp = cv[:]
                tmp.append(nn)
                tmp[0] = cf + f
                q.append(tmp[:])
                v[nn] = tmp[:]
    
    return v


def solution(n, s, a, b, fares):
    answer = 0
    connection = [[] for _ in range(n + 1)]
    
    # 경로 저장
    for i in range(len(fares)):
        start, end, f = fares[i]
        
        connection[start].append([end, f])
        connection[end].append([start, f])

    # 시작점, a의 집, b의 집에서 다른 장소까지의 최소 경비 계산
    sv = findWay(n, s, connection)    
    av = findWay(n, a, connection)
    bv = findWay(n, b, connection)

    answer = av[s][0] + bv[s][0]

    # 최소 택시비 찾기
    for i in range(1, n + 1):
        if i != s and sv[i] != [] and av[i] != [] and bv[i] != []:
            tmp = sv[i][0] + av[i][0] + bv[i][0]
            if answer > tmp:
                answer = tmp
    
    return answer