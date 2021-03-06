'''
처음 풀이 - 빌딩을 하나씩 읽어나감
case_num = 0
for _ in range(10):
    land = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    tallest = 0
    for b in range(2,len(buildings) - 2):
        tallest = max(buildings[b - 2], buildings[b - 1], buildings[b + 1], buildings[b + 2])
        if tallest < buildings[b]:
            total += (buildings[b] - tallest)

    case_num += 1

    print(f'#{case_num} {total}')
'''
# 두번째 풀이-한 건물이 조망권을 얻으면 그 양 옆의 두 건물은 조망권을 얻지 못한다는 힌트를 받아서 재구현 
case_num = 0
for _ in range(10):
    land = int(input()) # 땅 크기
    buildings = list(map(int, input().split())) # 빌딩 높이
    total = 0
    tallest = 0
    b = 2
    # 현재 빌딩 양 옆을 비교해 조망권을 구함
    while b < len(buildings) - 2:
        tallest = max(buildings[b - 2], buildings[b - 1], buildings[b + 1], buildings[b + 2])
        if tallest < buildings[b]:
            total += (buildings[b] - tallest)
            b += 3 # 한 건물이 조망권을 얻으면 그 옆 두 칸 거리까지의 건물은 조망권을 얻지 못함
        else:
            b += 1

    case_num += 1

    print(f'#{case_num} {total}')