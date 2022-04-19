import math

# 누적 시간 계산하는 함수
def howMuchTime(in_t, out_t):
    minute = int(out_t[3]+out_t[4]) - int(in_t[3]+in_t[4])
    hour = int(out_t[0]+out_t[1]) - int(in_t[0]+in_t[1])
    if minute < 0:
        minute += 60
        hour -= 1
    
    total = hour*60 + minute
    
    return total


# 주차 요금 계산하는 함수(함수에서 콜 하는 것이기 때문에 글로벌 변수가 아니라서 매개변수에 다 넣어줘야 함)
def howMuchFee(time, bt, bf, ut, uf):
    if time <= bt:
        f = bf
    else:
        f = bf + math.ceil((time-bt)/ut) * uf
    
    return f
    

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    car_numbers = []
    in_time_records = []
    total_times = []
    
    # 주차 기록 확인
    for i in range(len(records)):
        record = list(records[i].split())

        # 해당 기록이 입차 기록이면
        if record[2] == 'IN':

            # 이전에 입차한 기록이 있으면
            if record[1] in car_numbers:
                # 해당 차번호 인덱스에 입차 시간 저장
                in_time_records[car_numbers.index(record[1])] = record[0]
            
            # 이전에 입차한 기록이 없으면
            else:
                car_numbers.append(record[1])       # 차 번호 등록
                in_time_records.append(record[0])   # 입차 시간 저장
                total_times.append(0)               # 누적 시간을 저장할 공간 만들어줌
        
        # 해당 기록이 출차 기록이면
        else:
            car_num_id = car_numbers.index(record[1])   # 차 번호 인덱스 찾기
            in_time = in_time_records[car_num_id]       # 입차 시간
            out_time = record[0]                        # 출차 시간
            time = howMuchTime(in_time, out_time)       # 주차한 시간 계산
            in_time_records[car_num_id] = 0             # 입차 기록 지우기
            total_times[car_num_id] += time             # 누적 시간에 주차한 시간 더하기
    
    # 출차 기록이 없는 경우 23시 59분에 출차한 것으로 간주하여 주차 시간 계산
    for i in range(len(in_time_records)):
        if in_time_records[i]:
            time = howMuchTime(in_time_records[i], '23:59')
            total_times[i] += time
    
    answer = []
    each_fees = [0] * len(total_times)
    
    # 각 차들의 주차 요금 계산
    for i in range(len(each_fees)):
        fee = howMuchFee(total_times[i], base_time, base_fee, unit_time, unit_fee)
        each_fees[i] = [car_numbers[i], fee]
    
    # 차 번호대로 오름차순 정렬
    each_fees.sort(key=lambda x:x[0])
    
    for i in range(len(each_fees)):
        answer.append(each_fees[i][1])
    
    return answer