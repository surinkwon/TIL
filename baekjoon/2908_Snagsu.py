# 상수
a, b = input().split()

def rev_num(num_st):
    new_num = int(num_st[0]) + (int(num_st[1]) * 10) + (int(num_st[2]) * 100)
    return new_num

if rev_num(a) > rev_num(b):
    print(rev_num(a))
else:
    print(rev_num(b))

