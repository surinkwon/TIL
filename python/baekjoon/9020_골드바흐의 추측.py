'''
에라토스테네스의 체 + 투포인터
'''
import sys

prime = []

# 에라토스테네스의 체로 소수 구하기
is_prime = [1] * 10001
for i in range(2, len(is_prime)):
    if is_prime[i]:
        prime.append(i)
        for j in range(i, len(is_prime), i):
            is_prime[j] = 0

T = int(input())
for _ in range(T):
    number = int(sys.stdin.readline())
    s = 0
    e = len(prime) - 1

    # 투포인터로 두 수의 합 구하기, 소수를 구했을 때 이미 정렬되어있고, 겹치는 수가 없기 때문에 투포인터 사용 가능
    while s <= e:
        if prime[s] + prime[e] == number:
            answer = (prime[s], prime[e])
            s += 1
            e -= 1
        elif prime[s] + prime[e] < number:
            s += 1
        else:
            e -= 1

    print(answer[0], answer[1])

