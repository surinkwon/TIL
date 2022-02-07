t = int(input())

for _ in range(t):
    test_lst = input().split()
    repeat_num = int(test_lst[0])
    new_string = ''

    for letter in test_lst[1]:
        new_string += letter * repeat_num
    
    print(new_string)
