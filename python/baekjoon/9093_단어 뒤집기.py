N = int(input())

for _ in range(N):
    string_lst = input().split()

    for i in range(len(string_lst)):
        for j in range(len(string_lst[i])-1, -1, -1):
            print(string_lst[i][j], end='')
        print(' ', end='')
    
    print()
    