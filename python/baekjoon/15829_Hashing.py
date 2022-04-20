'''
문제대로 구현
'''
L = int(input())
r = 31
M = 1234567891
string = input()

hash_num = 0

for i in range(len(string)):
    hash_num += (ord(string[i])-96) * (r ** i)

print(hash_num%M)