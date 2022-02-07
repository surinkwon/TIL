# 수들의 합
sum_num = int(input())
cnt = 0
num = 1

# 1부터 하나씩 더해가다가 
# 마지막 숫자가 남은 숫자보다 클 때는 더이상 더할 숫자가 없으므로
# 개수 반환
while num <= sum_num:
    sum_num -= num
    num += 1
    cnt += 1

print(cnt)