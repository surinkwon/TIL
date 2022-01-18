count_num = int(input())
num_list = input().split()

for i in range(count_num):
    num_list[i] = int(num_list[i])

print(min(num_list), max(num_list))