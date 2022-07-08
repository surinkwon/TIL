import sys

N, P = map(int, input().split())

guitar = [set() for _ in range(7)]

total = 0

for _ in range(N):
    string, fret = map(int, sys.stdin.readline().split())

    # 해당 기타줄을 누르고 있으면
    if guitar[string]:

        # 누르려는 프렛 수가 더 크면 누르고 횟수 한 번 추가
        if max(guitar[string]) < fret:
            guitar[string].add(fret)
            total += 1
        
        # 누르려는 수가 더 작으면
        else:

            # 이미 누르고 있었으면
            if fret in guitar[string]:

                # 해당 수가 나올 때까지 누르고 있던 높은 수 프렛에서 손 떼기
                while guitar[string] and max(guitar[string]) != fret:
                    total += 1
                    guitar[string].remove(max(guitar[string]))
            
            # 안 누르고 있었으면
            else:

                # 해당 수보다 더 작은 수가 나올 떼까지 높은 수 프렛에서 손 떼기
                while guitar[string] and max(guitar[string]) > fret:
                    total += 1
                    guitar[string].remove(max(guitar[string]))
                
                # 해당 프렛 누르기
                total += 1
                guitar[string].add(fret)

    # 해당 기타 줄을 안 누르고 있었으면 프렛 누르기
    else:
        guitar[string].add(fret)
        total += 1

print(total)
