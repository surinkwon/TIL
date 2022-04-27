'''
그냥 구현하면 됨
방향에 따라 거리를 계산하는 것이 중요
1-북, 2-남, 3-서, 4-동

처음엔 동근이의 방향에 따라 네 개로 나눠서 각각 조건을 구했는데 코드가 너무 길어서
겹치는 부분은 줄였다. 그런데 시간은 더 걸린다..
'''
import sys


def calDistance():
    total = 0
    ddirection = dong[0] - 1
    ddistance = dong[1]

    # 북남 / 동서에 따라 반대편 방향에 있을 때 더해줘야 하는 변이 다르기 때문에
    # 미리 정해줌
    if ddirection == 0 or ddirection == 1:
        main = N
        sub = M
    else:
        main = M
        sub = N

    # 동근이 방향이 북서일 때
    if ddirection % 2 == 0:
        for i in range(len(companies)):
            direction = companies[i][0] - 1
            distance = companies[i][1]

            # 회사 방향이 동근이 방향과 같으면 
            if direction == ddirection:
                total += abs(distance - ddistance)
            
            # 회사 방향이 반대편이면
            elif direction == (ddirection + 1) % 4:
                tmp = main + ddistance + distance
                total += min(tmp, 2*N+2*M-tmp)
            
            # 회사 방향이 동, 남일 때
            elif direction == (ddirection + 2) % 4:
                total += distance + ddistance
            
            # 회사 방향이 서, 북일 때
            else:
                total += distance + sub - ddistance

    # 남동일 때
    else:
        for i in range(len(companies)):
            direction = companies[i][0] - 1
            distance = companies[i][1]

            if direction == ddirection:
                total += abs(distance - ddistance)
            elif direction == (ddirection + 3) % 4:
                tmp = main + ddistance + distance
                total += min(tmp, 2*N+2*M-tmp)
            elif direction == (ddirection + 1) % 4:
                total += main - distance + ddistance
            else:
                total += main - distance + sub - ddistance

    return total

M, N = map(int, input().split())
company_num = int(input())
companies = []
for _ in range(company_num):
    companies.append(list(map(int, sys.stdin.readline().split())))


dong = list(map(int, input().split()))

rlt = calDistance()

print(rlt)