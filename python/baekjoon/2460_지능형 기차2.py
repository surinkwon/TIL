max_passenger = 0
passenger_n = 0
for _ in range(10):
    out_num, in_num = map(int, input().split())
    passenger_n += in_num - out_num
    if max_passenger < passenger_n:
        max_passenger = passenger_n

print(max_passenger)

