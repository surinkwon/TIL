def findSet(str):
    lst = []
    for i in range(len(str) - 1):
        if ('a' <= str[i] <= 'z' or 'A' <= str[i] <= 'Z') and ('a' <= str[i+1] <= 'z' or 'A' <= str[i+1] <= 'Z'):
            s1, s2 = str[i], str[i+1]
            if 'A' <= s1 <= 'Z':
                s1 = chr(ord(s1)+32)
            if 'A' <= str[i+1] <= 'Z':
                s2 = chr(ord(s2)+32)
            lst.append(s1+s2)
    return lst


def findNum(s_lst, str_lst):
    num_lst = [0] * len(s_lst)
    i = j = 0
    while i < len(s_lst) and j < len(str_lst):
        if s_lst[i] == str_lst[j]:
            num_lst[i] += 1
            j += 1
        else:
            i += 1
    
    return num_lst


def solution(str1, str2):
    answer = 0
    
    # 대문자를 소문자로 바꿔서 두글자씩 나눠서 리스트에 저장
    str1_set_list = findSet(str1)
    str2_set_list = findSet(str2)
    
    
    # 각 문자들을 셋으로 합쳐주고 리스트로 변환
    sum_set = set(str1_set_list)
    for i in range(len(str2_set_list)):
        sum_set.add(str2_set_list[i])
    sum_set = list(sum_set)

    # 좀 더 빨리 수를 구하기 위해 정렬
    str1_set_list.sort()
    str2_set_list.sort()
    sum_set.sort()

    # 합집합 개수, 교집합 개수
    sum_num = inter_num = 0

    # 두 리스트 모두 각 문자가 몇개 들었는지 세어줌
    str1_num_list = findNum(sum_set, str1_set_list)  
    str2_num_list = findNum(sum_set, str2_set_list)
    
    # 합집합은 해당 문자 개수의 최대, 교집합은 해당 문자 개수의 최소
    for i in range(len(sum_set)):
        sum_num += max(str1_num_list[i], str2_num_list[i])
        inter_num += min(str1_num_list[i], str2_num_list[i])
    
    if sum_num:
        answer = int((inter_num/sum_num)*65536)
    else:
        answer = 65536
        
    return answer

a = solution('handshake', 'shake hands')
print(a)