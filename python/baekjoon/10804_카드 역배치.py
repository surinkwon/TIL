# 범위가 주어지면 그 번위 내 수를 뒤바꾸는 함수
def reverse(lst, start, end):
    while start < end:
        tem = lst[start]
        lst[start] = lst[end]
        lst[end] = tem

        start += 1
        end -= 1
    
    return lst

card = [i for i in range(1, 21)]

for _ in range(10):
    start, end = map(int, input().split())
    card = reverse(card, start - 1, end - 1)

print(f'{" ".join([str(i) for i in card])}')