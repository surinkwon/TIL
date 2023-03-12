# dp 배열 값의 의미는 해당 수가 가질 수 있는 최장 증가 부분 수열 길이

N = int(input())

numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    cur_max_num = 0

    for j in range(i - 1, -1, -1):
        if numbers[j] < numbers[i] and cur_max_num < dp[j]:
            cur_max_num = dp[j]
    
    dp[i] = cur_max_num + 1

print(max(dp))