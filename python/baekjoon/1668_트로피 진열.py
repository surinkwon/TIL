def see(lst):
    min_height = lst[0]
    can_see = 1
    for i in range(len(lst)):
        if lst[i] > min_height:
            min_height = lst[i]
            can_see += 1

    return can_see


# 트로피 개수
N = int(input())
# 왼쪽에서 볼 때, 오른쪽에서 볼 때
left = [0] * N
for i in range(N):
    left[i] = int(input())
right = left[::-1]

# 함수 돌려서 각각에 저장
left_see = see(left)
right_see = see(right)

print(left_see)
print(right_see)