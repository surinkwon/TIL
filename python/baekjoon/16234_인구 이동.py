'''
땅 전체를 확인하면서 국경을 열 구간을 정하고 반환
더이상 국경을 여는 곳이 없을 때까지 반복

주의할 것
- 변수 초기화하는 위치
- 카운트 세는 위치
- 각 반복문이 무슨 일을 하는지 정확하게 알기
- 꼭 모든 행렬 칸을 돌아야 하는지 한 번 생각해보기
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 국경을 열 나라와 그 구간의 인구를 반환하는 함수
def howManyDays(r, c):
    global v
    q = deque()
    q.append((r, c))
    v[r][c] = 1
    s = land[r][c]
    country = [(r, c)]

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and L <= abs(land[cr][cc]-land[nr][nc]) <= R:
                q.append((nr, nc))
                country.append((nr, nc))
                s += land[nr][nc]
                v[nr][nc] = 1

    return country, s


N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
# 인구 이동을 하는 횟수
pop_mov = 0
cnt = 1

# 인구 이동을 할 수 있을 때까지(하루에 인구 이동을 국경을 연 나라들끼리 모두 한다고 하면 그 하루를 말함)
while cnt:
    # 인구 이동을 하는 나라가 있는지 보는 변수
    cnt = 0
    # 하루에 어떤 나라들이 인구 이동을 하는지 알아야하기 때문에 전역변수로 둠
    # 국경을 여는 모든 나라가 같은 국경을 맞대고 있다고 장담할 수 없기 때문에
    # 국경을 맞대면서 인구 이동 할 수 있는 범위를 각각 구해줘야 하므로 하루마다 땅 전체를 봐야함
    # 그런데 이미 인구이동을 한 나라는 세줄 필요가 없기 때문에 전역변수로 두는 것
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        # 모든 칸을 돌 필요는 없음. 왜냐하면 하나의 칸에 대해 상하좌우를 모두 검사하므로
        # 격자로 돌면 모든 구역을 다 검사할 수 있음(다른 사람 풀이 보고 추가)
        for j in range(i%2, N, 2):
            # 해당 나라가 인구 이동을 한 적이 없으면
            if v[i][j] == 0:
                # 그 나라와 인구 이동할 나라를 모두 구하고 인구수 합을 구함
                open_gates, population_sum = howManyDays(i, j)
                
                # 지금 검사하려고 하는 나라는 무조건 들어가있으므로 국경을 연 나라가 하나보다 더 많을 때 작업해줌
                if len(open_gates) > 1:
                    pop = population_sum // len(open_gates)
                    for k in range(len(open_gates)):
                        land[open_gates[k][0]][open_gates[k][1]] = pop
                    
                    # 인구 이동을 했으면 카운트
                    cnt = 1

    pop_mov += 1

print(pop_mov - 1)






