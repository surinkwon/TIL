def solution(str1, str2):
    answer = 0
    
    str1_set_list = []
    str2_set_list = []
    
    # 대문자를 소문자로 바꿔서 두글자씩 나눠서 리스트에 저장
    for i in range(len(str1) - 1):
        if ('a' <= str1[i] <= 'z' or 'A' <= str1[i] <= 'Z') and ('a' <= str1[i+1] <= 'z' or 'A' <= str1[i+1] <= 'Z'):
            s1, s2 = str1[i], str1[i+1]
            if 'A' <= s1 <= 'Z':
                s1 = chr(ord(s1)+32)
            if 'A' <= str1[i+1] <= 'Z':
                s2 = chr(ord(s2)+32)
            str1_set_list.append(s1+s2)
    
    for i in range(len(str2) - 1):
        if ('a' <= str2[i] <= 'z' or 'A' <= str2[i] <= 'Z') and ('a' <= str2[i+1] <= 'z' or 'A' <= str2[i+1] <= 'Z'):
            s1, s2 = str2[i], str2[i+1]
            if 'A' <= str2[i] <= 'Z':
                s1 = chr(ord(s1)+32)
            if 'A' <= str2[i+1] <= 'Z':
                s2 = chr(ord(s2)+32)
            str2_set_list.append(s1+s2)
    
    # 각 문자들을 셋으로 합쳐주고 리스트로 변환
    sum_set = set(str1_set_list)
    for i in range(len(str2_set_list)):
        sum_set.add(str2_set_list[i])
    sum_set = list(sum_set)

    sum_num = inter_num = 0             # 합집합 개수, 교집합 개수
    str1_num_list = [0] * len(sum_set)  # 각 문자들의 수를 세줄 배열
    str2_num_list = [0] * len(sum_set)

    # 좀 더 빨리 수를 구하기 위해 정렬
    str1_set_list.sort()
    str2_set_list.sort()
    sum_set.sort()
    
    # 두 리스트 모두 각 문자가 몇개 들었는지 세어줌
    i = j = 0
    while i < len(sum_set) and j < len(str1_set_list):
        if sum_set[i] == str1_set_list[j]:
            str1_num_list[i] += 1
            j += 1
        else:
            i += 1
            
    i = j = 0        
    while i < len(sum_set) and j < len(str2_set_list):
        if sum_set[i] == str2_set_list[j]:
            str2_num_list[i] += 1
            j += 1
        else:
            i += 1
    
    # 합집합은 해당 문자 개수의 최대, 교집합은 해당 문자 개수의 최소
    for i in range(len(sum_set)):
        sum_num += max(str1_num_list[i], str2_num_list[i])
        inter_num += min(str1_num_list[i], str2_num_list[i])
    
    if sum_num:
        answer = int((inter_num/sum_num)*65536)
    else:
        answer = 65536
        
    return answer