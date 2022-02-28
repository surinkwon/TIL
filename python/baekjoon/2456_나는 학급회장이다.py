# 동률에서 회장 후보 정하는 함수
def president(a, b, matrix):
    if matrix[a][2] > matrix[b][2]:
        return a
    elif matrix[a][2] < matrix[b][2]:
        return b
    else:
        if matrix[a][1] > matrix[b][1]:
            return a
        elif matrix[a][1] < matrix[b][1]:
            return b
        else:
            return -1


N = int(input())
vote = [list(map(int, input().split())) for _ in range(N)]
cd = [[0] * 3 for _ in range(3)] # 각 행은 후보자 번호 인덱스, 각 열은 투표 점수 인덱스

for j in range(3):
    for i in range(N):
        cd[j][vote[i][j] - 1] += 1

total = [0] * 3
for i in range(len(total)):
    for j in range(len(total)):
        total[i] += cd[i][j] * (j + 1)

if total.count(max(total)) == 1:
    print(f'{total.index(max(total)) + 1} {max(total)}')
else:
    # 두개만 동률일 때를 검사하려면 나무지 하나가 동률이 아니라는 조건도 넣어줘야 한다
    if total[0] == total[1] and total[2] != total[0]: 
        cn = president(0, 1, cd)
        print(f'{cn + 1} {max(total)}')
    elif total[0] == total[2] and total[1] != total[0]:
        cn = president(0, 2, cd)
        print(f'{cn + 1} {max(total)}')
    elif total[1] == total[2] and total[2] != total[0]:
        cn = president(1, 2, cd)
        print(f'{cn + 1} {max(total)}')
    else:
        cn = president(0, 1, cd)
        if cn == -1:
            cn = president(0, 2, cd)
            print(f'{cn + 1} {max(total)}')
        else:
            cn = president(cn, 2, cd)
            print(f'{cn + 1} {max(total)}')
        

