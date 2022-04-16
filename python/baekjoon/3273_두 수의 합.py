'''
투포인터(서로 다른 정수들일때 사용하기 좋음), 두 수의 합
'''
N = int(input())
nums = sorted(list(map(int, input().split())))
X = int(input())

p1, p2 = 0, N - 1
cnt = 0

while p1 < p2:
    if nums[p1] + nums[p2] == X:
        cnt += 1
        # 두 수의 합이 목표값과 같으면 수를 키우거나 수를 줄이면 목표값과 달라지기때문에
        # 둘 다 해줌
        p1 += 1
        p2 -= 1
    # 목표값보다 두 수의 합이 작으면 수를 키워줘야 함
    elif nums[p1] + nums[p2] < X:
        p1 += 1
    # 목표값보다 두 수의 합이 크면 수를 줄여줘야 함
    else:
        p2 -= 1

print(cnt)
