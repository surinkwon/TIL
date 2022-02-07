sin_num = 0
while True:
    o, w = map(int, input().split())
    if o:
        status = ''
        died = 0
        while True:
            action, num = input().split()
            if action != '#':
                if action == 'F':
                    w += int(num)
                else:
                    w -= int(num)
                
                if w <= 0:
                    died = 1
            else:
                if o / 2 < w < 2 * o:
                    status = 'happy'
                elif w > 0:
                    status = 'sad'
                sin_num += 1
                break
        
        if died:
            print(f'{sin_num} RIP')
        else:
            if status == 'happy':
                print(f'{sin_num} :-)')
            else:
                print(f'{sin_num} :-(')
    else:
        break