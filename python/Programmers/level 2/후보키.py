from itertools import combinations

def solution(relation):
    new_table = list(zip(*relation))
    answer = 0
    cant = []       # 하나만으로는 후보키가 될 수 없는 열들

    # 단일키가 후보키가 될 수 있는지 판별
    # 혼자만으로 후보키가 될 수 있으면 나머지 후보키에는 끼지 못함 
    for i in range(len(new_table)):
        if len(set(new_table[i])) == len(relation):
            answer += 1
        else:
            cant.append(i)
    
    # 하나만으로 후보키가 될 수 없는 열들의 조합을 모두 구함
    possible = []
    for i in range(2, len(cant) + 1):
        possible += list(combinations(cant, i))
    
    # 해당 열 조합이 후보키가 될 수 있는지 판별
    for p in range(len(possible)):

        # 배열에서 pop을 해줄 것이기 때문에 현재 인덱스가 배열의 크기를 넘어가면 멈춤
        if p >= len(possible):
            break

        tmp = set()
        for r in range(len(relation)):
            one = []

            # 각 행에 대한 현재 열 조합 결과를 셋에 추가
            for n in range(len(possible[p])):
                one.append(relation[r][possible[p][n]])
            tmp.add(tuple(one))
        
        # 셋 길이가 행 길이와 같다는 것은 후보키가 될 수 있다는 것
        if len(tmp) == len(relation):
            answer += 1

            # 현재 열 조합이 후보키가 될 수 있으면 해당 열 조합이 속한 다른 열 조합은 후보키가 될 수 없음
            # 이를 판별하고 후보군에서 제거
            tmp_p = [0] * len(possible)
            for j in range(len(possible[p])):
                for pp in range(p + 1, len(possible)):
                    if possible[p][j] in possible[pp]:
                        tmp_p[pp] += 1
                
                for pp in range(len(possible) - 1, p, -1):
                    if tmp_p[pp] == len(possible[p]):
                        possible.pop(pp)
                
    return answer