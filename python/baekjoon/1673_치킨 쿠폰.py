while True:
    try: 
        N, K = map(int, input().split())
        total = stamp = N # 처음 쿠폰 수만큼 치킨 +

        while stamp >= K:
            total += stamp // K
            # 도장을 사용하면 도장을 사용하여 얻은 치킨 쿠폰 개수 + 사용하고 남은 도장 개수가
            # 새로운 도장 개수가 됨
            stamp = stamp // K + stamp % K
        
        print(total)
    except:
        break