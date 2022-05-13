'''
투포인터
'''
import sys

N = int(input())
solutions = sorted(list(map(int, sys.stdin.readline().split())))
close = 30000000000
close_solutions = [0, 0]

s, e = 0, N - 1

while s < e:
    abs_sum_sol = abs(solutions[s] + solutions[e])
    sum_sol = solutions[s] + solutions[e]
    if sum_sol == 0:
        close_solutions = [solutions[s], solutions[e]]
        break
    elif sum_sol < 0:
        if close > abs_sum_sol:
            close = abs_sum_sol
            close_solutions = [solutions[s], solutions[e]]
        s += 1
    else:
        if close > abs_sum_sol:
            close = abs_sum_sol
            close_solutions = [solutions[s], solutions[e]]
        e -= 1


print(close_solutions[0], close_solutions[1])