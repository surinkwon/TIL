string = input()
ucpc_lst = [0] * 3

for i in range(len(string)):
    if string[i] == 'U':
        ucpc_lst[0] = 1
    elif string[i] == 'C':
        if ucpc_lst[0] and ucpc_lst[2]:
            ucpc_lst[1] += 1
        else:
            if ucpc_lst[0]:
                ucpc_lst[1] = 1
    elif string[i] == 'P':
        if ucpc_lst[1]:
            ucpc_lst[2] = 1

if ucpc_lst[0] and ucpc_lst[2] and ucpc_lst[1] > 1:
    print('I love UCPC')
else:
    print('I hate UCPC')
