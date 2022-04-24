T = int(input())

for _ in range(T):
    n = int(input())
    binary_n = ''

    while n != 0:
        binary_n += str(n % 2)
        n //= 2
    
    for i in range(len(binary_n)):
        if binary_n[i] == '1':
            print(i, end=' ')