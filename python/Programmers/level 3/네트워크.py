from collections import deque

# 하나의 네트워크에 연결된 컴퓨터 찾는 함수
def findNetwork(i, v, computers):
    q = deque()
    q.append(i)
    v[i] = 1
    
    while q:
        ci = q.popleft()
        
        for j in range(len(computers)):
            if not v[j] and computers[ci][j]:
                v[j] = 1
                q.append(j)
    return v

def solution(n, computers):
    answer = 0
    v = [0] * n
    
    # bfs로 연결된 컴퓨터 찾아서 제외하기
    for i in range(n):
        if not v[i]:
            answer += 1
            v = findNetwork(i, v, computers)
        
    return answer