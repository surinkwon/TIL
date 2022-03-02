for _ in range(3):
    numbers = list(map(int, input()))
    max_sq = sq = 0
    for i in range(1, len(numbers)):
        if numbers[i - 1] == numbers[i]:
            sq += 1
        else:
            if max_sq < sq + 1:
                max_sq = sq + 1
            sq = 0
    # 한 번 더 비교 안 해주면 끝까지 연속된 경우가 나왔을 때 0으로 출력됨
    if max_sq < sq + 1:
        max_sq = sq + 1
    print(max_sq)