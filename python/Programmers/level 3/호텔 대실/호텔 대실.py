# 시간 또는 분을 두 자리로 맞추는 함수
def padZero(num):
    if num < 10:
        return f'0{num}'
    return f'{num}'

# 시간 문자열을 숫자로 변환하는 함수
def turnTimeToInt(time_string):
    return int(time_string.replace(':', ''))

# 시간에 10분을 더하는 함수
def addTenMinute(time_string):
    [hour, minute] = time_string.split(':')
    hour = int(hour)
    minute = int(minute)
    minute += 10
    
    if minute >= 60:
        minute -= 60
        hour += 1
    
    return f'{padZero(hour)}:{padZero(minute)}'

def solution(book_time):
    START = 0
    END = 1
    
    # 예약 내역 숫자로 변경
    for i in range(len(book_time)):
        [start_time, end_time] = book_time[i]
        book_time[i] = [turnTimeToInt(start_time), turnTimeToInt(addTenMinute(end_time))]
    
    # 예약 내역 시작시간 빠른 순, 끝 시작 빠른 순으로 정렬
    book_time.sort(key = lambda x: [x[0], x[1]])
    
    # 방 배정
    room = [book_time[0][END]]
    
    for i in range(1, len(book_time)):
        j = 0
        
        while j < len(room) and room[j] > book_time[i][START]:
            j += 1
        
        # 배정할 수 있는 방이 없으면 방 추가
        if j == len(room):
            room.append(book_time[i][END])
        # 배정할 방이 있으면 배정
        else:
            room[j] = book_time[i][END]
    
    return len(room)