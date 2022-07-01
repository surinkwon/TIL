dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C = map(int, input().split())

current_map = [list(input()) for _ in range(R)]
used_to_island = [[0] * C for _ in range(R)]

# 50년 후 지도 만들기
for r in range(R):
    for c in range(C):
        if current_map[r][c] == 'X':
            sea = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < R and 0 <= nc < C and current_map[nr][nc] == '.' and used_to_island[nr][nc] == 0:
                    sea += 1
                elif 0 > nr or R <= nr or 0 > nc or C <= nc:
                    sea += 1
            
            if sea > 2:
                current_map[r][c] = '.'
                used_to_island[r][c] = 1

# 50년 후 지도 크기 편집
first_r = last_r = -1   # 0행부터 섬이 있을 수 있으니 -1로 초기화
first_c = C
last_c = 0

# 가장 좌측에 있는 섬과 가장 우측에 있는 섬 찾기
for r in range(R):
    if 'X' in current_map[r]:
        # 가장 위쪽 섬 찾기
        if first_r != -1:
            last_r = r
        else:
            first_r = r
        
        c = 0
        while current_map[r][c] == '.':
            c += 1
        
        if first_c > c:
            first_c = c
        
        c = C - 1

        while current_map[r][c] == '.':
            c -= 1
        
        if last_c < c:
            last_c = c

# 섬이 한 줄에 있을 경우 처리
if last_r == -1:
    last_r = first_r

for r in range(first_r, last_r + 1):
    for c in range(first_c, last_c + 1):
        print(current_map[r][c], end='')
    print()

