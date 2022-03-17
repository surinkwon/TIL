# 바이너리 서치 함수
def bi(lst, g):
    mid = (len(lst) - 1) // 2
    start = 0
    end = len(lst) - 1

    while start <= end:
        if g == lst[mid]:
            return 1
        elif g > lst[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
    
    return 0

N = int(input())
data = sorted(list(map(int, input().split())))
M = int(input())
search_this = list(map(int, input().split()))

for i in range(M):
    rlt = bi(data, search_this[i])
    print(rlt)
