'''
조건만 잘 지정하면 됨
'''

# 거리두기 검사 함수
def isRight(place):
    for i in range(len(place)):
        for j in range(len(place)):
            # 현재 자리에 사람이 있으면
            if place[i][j] == 'P':
                # 그 바로 옆이나 아래에 사람이 있으면 거리두기 X
                if (j + 1 < len(place) and place[i][j+1] == 'P') or (i + 1 < len(place) and place[i+1][j] == 'P'):
                    return 0
                # 오른쪽 아래에 사람이 있는데
                if i + 1 < len(place) and j + 1 < len(place) and place[i+1][j+1] == 'P':
                    # 파티션이 하나라도 없으면 거리두기 X
                    if place[i][j+1] != 'X' or place[i+1][j] != 'X':
                        return 0
                # 왼쪽 아래에 사람이 있는데
                if i + 1 < len(place) and j - 1 > -1 and place[i+1][j-1] == 'P':
                    # 파티션이 하나라도 없으면 거리두기 X
                    if place[i][j-1] != 'X' or place[i+1][j] !='X':
                        return 0
                # 오른쪽 옆 2칸 위치에 사람이 있는데 파티션이 사이에 없으면 거리두기 X
                if i + 2 < len(place) and place[i+2][j] == 'P':
                    if place[i+1][j] != 'X':
                        return 0
                # 왼쪽 옆 2칸 위치에 사람이 있는데 파티션이 사이에 없으면 거리두기 X
                if j + 2 < len(place) and place[i][j+2] == 'P':
                    if place[i][j+1] != 'X':
                        return 0
    
    return 1


def solution(places):
    answer = []
    
    # 대기실 별로 거리두기 지키는지 확인
    for place in range(len(places)):
        rlt = isRight(places[place])
        answer.append(rlt)
        
    return answer

p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

a = solution(p)
print(a)