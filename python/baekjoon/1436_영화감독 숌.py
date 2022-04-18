'''
666부터 해당 길이까지 숫자 찾기
패턴을 찾으려고 했는데 도저히 못 찾겠고 없는 것 같아서 알고리즘 분류가 브루트포스라 이렇게 짰다...
'''

N = int(input())
cnt = 0
i = 666
nums = set()
while True:
    # 666부터 수를 증가시키며 해당 수 안에 666이 있으면 셋에 저장
    if '666' in str(i):
        nums.add(int(i))
        cnt += 1
    
    # 셋에 저장된 수의 개수가 찾는 수라면 출력
    if cnt == N:
        nums_lst = list(nums) # 이렇게 해서 정렬하고 맨 앞의 거 출력하는 거랑 그냥 여기서 바로 출력하는 거랑 시간 차이 없음...
        break
    i += 1

nums_lst.sort(reverse=True)
print(nums_lst[0])
    