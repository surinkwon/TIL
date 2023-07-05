def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    
    # 신고 데이터를 저장할 2차원 배열
    re = [[0] * len(id_list) for _ in range(len(id_list))]
    
    # 행 인덱스가 신고 받은 사람, 열 인덱스가 신고 한 사람
    for i in range(len(report)):
        reporter, reported = list(report[i].split())

        # 중복을 방지하기 위해 신고자가 누구를 신고 했다는 표시만 해줌
        re[id_list.index(reported)][id_list.index(reporter)] = 1
    
    # 신고 횟수가 k보다 많으면 그 사람을 신고한 사람들에게 메일 보낼 횟수 추가
    for i in range(len(re)):
        if sum(re[i]) >= k:
            for j in range(len(re[0])):
                if re[i][j]:
                    answer[j] += 1
            
    return answer