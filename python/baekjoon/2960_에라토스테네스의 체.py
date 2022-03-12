# 소수를 차례대로 처리하는 함수
def eratos(total, num):
    lst = [1 for _ in range(total + 1)]
    right = 0

    for i in range(2, len(lst)):
        if lst[i]:
            for j in range(i, len(lst), i):
                if lst[j]:
                    lst[j] = 0
                    right += 1
                    if right == num:
                        return j

N, K = map(int, input().split())

rlt = eratos(N, K)

print(rlt)