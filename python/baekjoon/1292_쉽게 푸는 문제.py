A, B = map(int, input().split())

# 각 숫자마다 해당 숫자 개수만큼 리스트를 만듦
# A에 1이 들어올 수도 있으므로 0번째 리스트도 만들어줌
numbers = [[0]] + [[i] * i for i in range(1, B + 1)]

cnt = 0
i = 0
min_sum = max_sum = 0

while i < len(numbers):
    j = 0
    # A부터 B번째 수까지의 합이므로 A전까지의 합을 min_sum에 저장
    while j < len(numbers[i]):
        if cnt < A:
            min_sum += numbers[i][j]
        
        # B까지의 합을 max_sum에 저장
        if cnt < B + 1:
            max_sum += numbers[i][j]
        
        j += 1
        cnt += 1

        # B를 넘어가면 반복문 빠져나옴
        if cnt == B + 1:
            break
    
    i += 1
    if cnt == B + 1:
            break

print(max_sum - min_sum)