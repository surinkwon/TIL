N, kim, im = map(int, input().split())
r = 0 # 라운드

# 번호가 홀수면 2로 나눈 몫에 1을 더한 값이 다음 번호가 됨
# 짝수면 2로 나눈 몫이 다음 번호가 됨
while kim != im:
    kim = kim // 2 + 1 if kim % 2 else kim // 2
    im = im // 2 + 1 if im % 2 else im // 2

    r += 1

print(r)