# bfs 함수 k값 초기화 주의하기!!
def dfs(start, c):
    visited = [0]           # 방문 리스트
    stack = [0] * len(c)    # 스택
    # 스택 탑 인덱스, 탑을 -1로 설정하면 탑 +1을 하고 스택에 시작점을 추가해야 하기 때문에
    # 처음부터 0으로 지정해줌
    top = 0 
    visited[0] = start      # 방문리스트와 스택에 시작점 추가
    stack[top] = start
    k = 0                   # k는 해당 정점에서 방문할 수 있는 정점 리스트의 인덱스를 의미

    # 스택이 비어있지 않는 동안, 갈 수 있는 경로가 있는 동안
    while top > -1:

        # 해당 정점에서 갈 수 있는 정점이 있는지 조회
        # K의 범위를 지정해주는 이유는 인덱스 에러를 방지하기 위함
        if c[stack[top]] and k < len(c[stack[top]]):

            # 갈 수 있는 정점이 아직 방문하지 않은 정점이면
            if  c[stack[top]][k] not in visited:
                visited.append(c[stack[top]][k])    # 방문 리스트에 해당 정점 추가
                point = stack[top]                  # 현재 정점은 스택의 탑에 있는 정점
                top += 1                            # 스택에 방문할 수 있는 정점 push
                stack[top] = c[point][k]
                # 스택에 push한 정점으로 이동하면 그 정점에서 방문할 수 있는 정점을 처음부터 조회해야 하므로
                # 초기화해줌
                k = 0 

            # 갈 수 있는 정점이 이미 방문한 정점이라면 다른 갈 수 있는 정점을 찾음
            else:
                k += 1
        
        # 더이상 갈 수 있는 정점이 없으면 pop하고 해당 정점부터 다시 탐색
        else:
            top -= 1
            k = 0

    
    return visited


def bfs(s, c):
    visited = [0]               # 방문 리스트
    queue = [0] * len(c)        # 큐
    qf = -1
    qr = 0                      # 스택 탑과 같은 이유로 처음에는 0으로 설정
    visited[0] = S              # 방문 리스트와 큐에 시작점 추가
    queue[qr] = s

    while qf != qr:                             # 큐가 비어있지 않으면, 갈 수 있는 정점이 있으면
        qf += 1                                 # 디큐한 후 해당 정점을 기준으로 삼음
        point = queue[qf]

        if c[point]:                            # 기준 정점에서 갈 수 있는 정점이 있으면
            for i in range(len(c[point])):      # 갈 수 있는 모든 정점을 조회
                if c[point][i] not in visited:  # 아직 방문하지 않은 정점이라면
                    visited.append(c[point][i]) # 방문 리스트에 추가 및 인큐
                    qr += 1
                    queue[qr] = c[point][i]
    
    return visited



N, M, S = map(int, input().split())
connected = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    if j not in connected[i]:
        connected[i].append(j)
    if i not in connected[j]:
        connected[j].append(i)

# 방문 가능한 정점이 여러 개면 번호가 작은 정점부터 방문해야 하므로 정렬해줌
for i in range(1, len(connected)):
    connected[i] = sorted(connected[i])


road1 = dfs(S, connected)
road2 = bfs(S, connected)

print(' '.join([str(x) for x in road1]))
print(' '.join([str(x) for x in road2]))
