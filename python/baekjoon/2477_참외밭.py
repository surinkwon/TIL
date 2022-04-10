'''
ㄱ자 넓이를 구하려면 큰 사각형에서 작은 사각형을 빼면 되는데
큰 사각형의 변은 방향이 하나만 나오는 경우이고
작은 사각형의 변은 앞뒤로 큰 사각형의 변이 나오지 않는 경우이다.
이를 고려해서 각 변을 구하고 넓이를 구해 빼면 된다.
'''

K = int(input())
# 방향과 길이를 담을 배열
direction = [0] * 6
lengths = [0] * 6

# 방향과 길이를 담음
for i in range(6):
    d, l = map(int, input().split())
    direction[i] = d
    lengths[i] = l

b = s = 1

for i in range(6):
    # 방향이 한 번만 나오면 큰 사각형의 넓이에 곱함
    if direction.count(direction[i]) == 1:
        b *= lengths[i]
    # 방향이 두 번 나오면
    else:
        # 앞뒤에 큰 사각형의 변이 나오지 않는다면 작은 사각형의 넓이에 곱함
        if direction.count(direction[(i+5)%6]) != 1 and direction.count(direction[(i+1)%6]) != 1:
            s *= lengths[i]

print((b-s)*K)


    
