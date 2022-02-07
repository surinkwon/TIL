test_num = int(input())

for _ in range(test_num):
    cal_list = list(input().split())
    num = float(cal_list[0])
    
    for ind in cal_list[1:]:
        if ind == '@':
            num *= 3
        
        elif ind == '#':
            num -= 7
        
        else:
            num += 5
    print('%0.2f' %num)
