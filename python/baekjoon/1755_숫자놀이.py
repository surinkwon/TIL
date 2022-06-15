alph_num = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
'6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

M, N = map(int, input().split())
rlt = []

for num in range(M, N + 1):
    string_num = str(num)
    n_str = ''
    for i in range(len(string_num)):
        n_str += alph_num[string_num[i]]
    
    rlt.append([n_str, num])

rlt.sort(key=lambda x: x[0])

for i in range(len(rlt)):
    if i != 0 and i % 10 == 0:
        print()
    print(rlt[i][1], end=' ')