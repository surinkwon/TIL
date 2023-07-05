'''
순서대로 찍어야 하는 스킬의 순서가 주어지고 이를 통해 주어지는 스킬트리 중 
몇 개가 가능한지 구하는 문제

스킬의 인덱스를 이용해 해당 스킬이 지금 찍을 수 있는 스킬인지 판별
'''

def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    
    for i in range(len(skill_trees)):
        now_order = 0
        for j in range(len(skill_trees[i])):
            now_skill = skill_trees[i][j]
            if now_skill in skill_set:
                if now_order == skill.index(now_skill):
                    now_order += 1
                else:
                    # 맨 마지막 스킬에서 불가능하다고 판별날 수 있으므로 예외 처리 해줌
                    j -= 1
                    break
        if j == len(skill_trees[i]) - 1:
            answer += 1
            
    return answer