import sys

N = int(input())
s = 0               # 수들의 합
num_dict = {}       # 수의 빈도를 담을 딕셔너리
nums_set = set()    # 수가 앞에 나온 적이 있는지 빨리 탐색하기 위해 셋을 만들어줌
nums = [0] * N      # 수들을 담을 배열

for i in range(N):
    nums[i] = int(sys.stdin.readline())     # 수를 배열에 담음
    s += nums[i]                            # 합에 더함
    if nums[i] not in nums_set:             # 앞에 나온 적 없는 수면
        nums_set.add(nums[i])               # 셋에 추가
        num_dict.update({nums[i]:1})        # 딕셔너리에 키, 값 생성
    else:
        num_dict[nums[i]] += 1              # 앞에 나온 적이 있으면 빈도수 +

nums.sort()                 # 중앙값을 찾기 위해 정렬
av = round(s/N)             # 평균 구하기
mid = nums[N//2]            # 중앙값 찾기
ra = nums[N-1] - nums[0]    # 범위 구하기
mode_lst = []               # 최빈값을 구하기 위한 리스트


for key, value in num_dict.items():         # 빈도 딕셔너리를 리스트로 바꿔줌
    mode_lst.append([key, value])

# 빈도 수가 같으면 두번째로 작은 값을 출력해야하므로 값은 내림차순, 키는 오름차순 정렬
mode_lst.sort(key=lambda x:(-x[1], x[0]))   

if len(mode_lst) > 1:
    # 빈도 수가 같은 게 있으면 
    if mode_lst[0][1] == mode_lst[1][1]:
        # 두번 째로 작은 값이 최빈값
        mode = mode_lst[1][0]
    else:
        # 아니면 그냥 최빈값
        mode = mode_lst[0][0]
else:
    mode = mode_lst[0][0]

print(av)
print(mid)
print(mode)
print(ra)
