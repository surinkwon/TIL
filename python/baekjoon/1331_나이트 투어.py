w = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
h = [6, 5, 4, 3, 2, 1]

# 나이트가 갈 수 있는 곳
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]
path = [0] * 36 # 나이트가 지나가는 길을 담을 리스트

# 시작점
first = input()
path[0] = first
r = h.index(int(first[1]))
c = w[first[0]]
result = 'Invalid'

for _ in range(36):
    if _ < 35:
        new = input()
        nr = h.index(int(new[1]))
        nc = w[new[0]]

        # 새로 가는 곳이 이미 들린 곳인지 검사(나이트 투어가 모든 칸을 한 번씩 방문하는 것이므로)
        if new in path:
            result = 'Invalid'
            break
        else:
            path[_ + 1] = new

        # 다음 칸이 나이트가 갈 수 있는 곳이면
        i = 0
        while i < len(dr):
            if r + dr[i] == nr and c + dc[i] == nc:
                r = nr
                c = nc
                break
            else:
                i += 1
        
        # 나이트가 갈 수 있는 곳이 아니면 검사 끝냄
        if i == len(dr):
            break

    else:
        # 마지막으로 들린 칸이면 맨 처음 칸으로 갈 수 있는지 검사
        nr = h.index(int(first[1]))
        nc = w[first[0]]
        i = 0

        while i < len(dr):
            if r + dr[i] == nr and c + dc[i] == nc:
                r = nr
                c = nc
                result = 'Valid'
                break
            else:
                i += 1
        
print(result)
