# 수열 변화시키는 함수
def change(lst):
    changed_lst = [0] * (len(lst) - 1)
    for i in range(len(changed_lst)):
        changed_lst[i] = lst[i + 1] - lst[i]

    return changed_lst

N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(K):
    A = change(A)

print(','.join([str(x) for x in A]))