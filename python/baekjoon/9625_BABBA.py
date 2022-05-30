K = int(input())

a_num = 1
b_num = 0

for _ in range(K):
    new_a_num = b_num
    new_b_num = b_num + a_num

    a_num = new_a_num
    b_num = new_b_num

print(a_num, b_num)

