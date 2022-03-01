N, score, P = map(int, input().split())

if N:
    pre_scores = list(map(int, input().split()))
    rank = 0

    # 랭킹이 꽉 차있을 때
    if N == P:
        # 현재 점수가 랭킹의 점수보다 클 때만 랭킹에 들어갈 수 있음
        for i in range(N):
            if score > pre_scores[i]:
                rank = i + 1
                break
        
        # 랭킹이 매겨졌다면 일단 랭킹안에 들어와 있다는 것
        if rank:
            # 랭킹에 들어올 때 현재 이전 점수들보다 큰 점수일때로 매겨지기 때문에
            # 랭킹의 앞부분에 현재점수와 같은 점수가 있을 수 있음
            # 그런 경우 그 점수들까지 고려해서 랭킹을 내야 함(가장 작은 등수로)
            if score == pre_scores[rank - 2]:
                i = 2
                while rank - 1 - i >= 0 and pre_scores[rank - 1 - i] == score:
                    i += 1
                print(rank - i + 1)
            else:
                print(rank)
        # 랭킹이 매겨지지 않았다면 점수가 너무 작음
        else:
            print(-1)
    
    # 랭킹이 꽉 차지 않았을 때
    else:
        for i in range(N):
            if score >= pre_scores[i]:
                rank = i + 1
                break
        # 랭킹이 매겨졌다면 그대로 출력
        if rank:
            print(rank)
        # 랭킹이 매겨지지 않았다면 그 다음 랭크로 들어감
        else:
            print(N + 1)
else:
    print(1)
