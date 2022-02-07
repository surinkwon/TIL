# 최대, 몇번째인지 구하기
num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for a in range(9):
    num_list[a] = int(input())

for i in range(len(num_list)):
    if num_list[i] == max(num_list):
        print(max(num_list))
        print(i + 1)