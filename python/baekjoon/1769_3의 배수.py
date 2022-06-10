num = input()
cnt = 0

while int(num) // 10 != 0:
    new_num = 0

    for i in range(len(num)):
        new_num += int(num[i])
    
    num = str(new_num)
    cnt += 1

print(cnt)
if num == '3' or num == '6' or num == '9':
    print('YES')
else:
    print('NO')