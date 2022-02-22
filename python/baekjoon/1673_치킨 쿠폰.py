while True:
    try: 
        N, K = map(int, input().split())
        total = stamp = N # 처음 쿠폰 수만큼 치킨 +

        while stamp >= K:
            total += stamp // K
            stamp = stamp // K + stamp % K # 도장 수는 이렇게 갱신됨
        
        print(total)
    except:
        break