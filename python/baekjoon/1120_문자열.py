# 문자열에 서로 다른 것이 얼마나 있는지 반환하는 함수
def same(shorter, longer, id):
    dif = 0
    for i in range(len(shorter)):
        if shorter[i] != longer[id + i]:
            dif += 1
    
    return dif


A, B = input().split()
min_d = 987654321

for j in range(len(B) - len(A) + 1):
    differ = same(A, B, j)
    if min_d > differ:
        min_d = differ

print(min_d)
