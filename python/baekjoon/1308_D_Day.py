'''
날짜 계산은 현재 연도와 디데이 연도를 제외한 나머지 연도들의 날짜를 모두 더해준 후
현재 연도에서 다음 연도까지 남은 날을 더해주고
디데이 연도의 시작에서 디데이까지 지난 날짜를 더해주는 방식으로 계산
'''

month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_mday = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 현재 연도에서 지나온 날짜 계산 함수
def plusDay(leap, month, day):
    after = 0
    if leap:
        for j in range(month):
            after += leap_year_mday[j]
    else:
        for j in range(month):
            after += month_day[j]
    
    after += day

    return after


# 윤년 확인하는 함수
def isLeap(num):
    if num % 400 == 0 or (num % 4 == 0 and num % 100):
        return 1
    else:
        return 0

# 현재 날짜와 디데이 날짜 받기
ty, tm, td = map(int, input().split())
dy, dm, dd = map(int, input().split())

# 각 년도가 윤년인지 검사
wty = isLeap(ty)
wdy = isLeap(dy)

left_day = 0

# 1000년 이상 차이가 나면 탈주
if dy - ty > 1000 or dy - ty == 1000 and (dm > tm or dm == tm and dd >= td):
    print('gg')
else:
    # 1000년 아래로 차이가 나면 차이나는 년도만큼 날짜 더해줌
    for i in range(ty+1, dy):
        if isLeap(i):
            left_day += sum(leap_year_mday)
        else:
            left_day += sum(month_day)

    # 월, 일 날짜 계산
    if ty != dy:
        if wty:
            days = plusDay(wty, tm, td)
            left_day += (sum(leap_year_mday) - days)

        else:
            days = plusDay(wty, tm, td)
            left_day += (sum(month_day) - days)

        left_day += plusDay(wdy, dm, dd)

    else:
        if wty:
            for i in range(tm, dm):
                left_day += leap_year_mday[i]
            
            left_day += dd - td
        else:
            for i in range(tm, dm):
                left_day += month_day[i]
            
            left_day += dd - td

    print(f'D-{left_day}')