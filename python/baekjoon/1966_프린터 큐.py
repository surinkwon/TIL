T = int(input())

for _ in range(T):
    N, find = map(int, input().split())
    pri = list(map(int, input().split()))
    max_value = max(pri)
    front = cnt = 0

    while True:
        # 가장 높은 우선순위가 뽑을 차례가 되었으면
        if max_value == pri[front]:
            # 그게 찾고자 하는 문서였으면
            if front == find:
                cnt += 1
                # 차례 출력
                print(cnt)
                break
            # 찾고자하는 문서가 아니었으면
            else:
                cnt += 1                # 차례 + 1
                pri[front] = 0          # 인쇄
                front += 1              # 다음 문서로 넘어감
                max_value = max(pri)    # 가장 높은 우선순위 갱신
       
        # 가장 앞에 놓인 것이 가장 높은 우선순위가 아니면
        else:
            pri.append(pri[front])      # 맨 뒤로 보냄
            pri[front] = 0              
            if front == find:           # 해당 문서가 찾고자하는 문서였으면
                find = len(pri) - 1     # 찾고자 하는 문서의 인덱스 갱신
            front += 1                  # 다음 문서로 넘어감
