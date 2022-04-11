'''
부분집합 구하기
'''


def findSubset(i, N, lst):
    # 원래 집합에서 각 원소를 포함 시킬 것인지 안 시킬 것인지를 판별하며 구하는 것이므로
    # 끝의 원소까지 보고 길이를 따져봐야 함
    if i == N:
        if len(lst) == 6:
            print(' '.join(lst))
    elif len(lst) > N:
        return
    else:
        lst.append(nums[i])
        findSubset(i+1, N, lst)
        lst.pop()
        findSubset(i+1, N, lst)

while True:
    nums = list(input().split())
    if nums[0] == '0':
        break
    else:
        K = int(nums[0])
        nums = nums[1:]
        findSubset(0, K, [])
        print()