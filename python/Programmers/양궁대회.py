'''
nonlocal을 쓰려면 함수 안에 함수를 정의해줘야 함
부분집합 합 구하는 것과 비슷한 방식으로 구현
얕은 복사 주의하기!!!!!
'''


def solution(n, info):
    beat = [0] * 11         # 라이언이 해당 점수를 얻기 위해 필요한 화살 개수 배열
    apeach_score = 0        # 어피치 점수
    max_d = 0               # 가장 큰 차이
    max_d_lst = []          # 가장 큰 차이일 때 라이언의 화살 데이터
    
    # 라이언이 점수를 얻기 위한 화살 개수와 어피치의 점수를 구함
    for i in range(len(info)-1):
        beat[i] = info[i] + 1
        if info[i]:
            apeach_score += 10 - i
    
    # 모든 경우의 수 구하기
    def calScores(i, N, beat_lst, a_s, l_s, l_info, arrow_num):
        nonlocal max_d, max_d_lst

        # 라이언이 쏜 화살 개수가 게임에서 사용할 수 있는 화살 개수와 같다면
        if arrow_num == N:
            
            # 점수 차이가 이전 점수 차이보다 크다면 정보 갱신
            if max_d < l_s - a_s:
                max_d = l_s - a_s
                max_d_lst = l_info[:]
            # 라이언의 점수가 더 크면서 점수 차이가 이전과 같다면
            elif l_s > a_s and max_d == l_s - a_s:
                for j in range(10, -1, -1):
                    '''
                    처음엔 아래 elif 구문을 안 써줘서 계속 에러가 났다...
                    저 구문을 안 써주면 거의 무조건 max_d_lst가 l_info로 바뀐다.
                    그런데 사실 max_d_lst의 가장 낮은 점수 화살 개수가 더 많으면 바꾸면 안 되기 때문에 조건을 추가해야 한다.
                    '''
                    if max_d_lst[j] < l_info[j]:        # 현재 라이언 화살에서 낮은 점수 화살 개수가 많으면
                        max_d_lst = l_info[:]           # 정보 갱신
                        break
                    elif max_d_lst[j] > l_info[j]:      # 이전이 더 많으면 그냥 넘어감
                        break
        
        elif i == 11:                                   # 점수 계산이 끝났는데
            if arrow_num < N:                           # 쏠 수 있는 화살이 남았으면
                if l_s > a_s and max_d <= l_s - a_s:    # 라이언 점수가 더 크고 둘의 차이가 이전보다 크거나 같으면 정보갱신
                    max_d = l_s - a_s
                    max_d_lst = l_info[:]
                    max_d_lst[10] += N - arrow_num      # 0점에 맞춘 화살 개수에 남은 화살을 모두 더해줌
        else:
            l_info[i] = beat_lst[i]
            if info[i]:
                tmp = a_s - (10-i)
            else:
                tmp = a_s
            
            # 라이언이 해당 점수를 얻었을 경우
            calScores(i+1, N, beat_lst, tmp, l_s+(10-i), l_info, arrow_num+beat_lst[i])
            l_info[i] = 0

            # 라이언이 해당 점수를 얻지 못했을 경우
            calScores(i+1, N, beat_lst, a_s, l_s, l_info, arrow_num)

    calScores(0, n, beat, apeach_score, 0, [0]*11, 0)
    
    # 정보가 갱신된 적 있으면 라이언이 이길 수 있다는 뜻이므로 정답 변수에 저장
    if max_d_lst:
        answer = max_d_lst
    # 갱신된 적 없으면 라이언은 이길 수 없으므로 -1 저장
    else:
        answer = [-1]
    return answer