# 케이스 번호
case = 1

while True:
    N = int(input())

    if N :
        # 마니또 연결 정보 딕셔너리
        manito_dict = {}
        givers = []
        total_chain = 0
        chain_names = set()

        # 마니또 정보 등록, 주는 사람 이름 저장
        for _ in range(N):
            giver, reciever = input().split()
            manito_dict[giver] = reciever
            givers.append(giver)
        
        # 체인 확인
        for i in range(N):
            giver = givers[i]
            if giver not in chain_names:
                while giver not in chain_names:
                    chain_names.add(giver)
                    giver = manito_dict[giver]
                total_chain += 1
        
        print(case, total_chain)
        case += 1
    else:
        break

