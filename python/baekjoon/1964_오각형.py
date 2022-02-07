stage = int(input())
dot_num = 5 + (((stage - 1) * (14 + (stage - 2) * 3)) // 2)
print(dot_num % 45678)