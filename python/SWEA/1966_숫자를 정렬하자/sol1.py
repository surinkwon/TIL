import sys

sys.stdin = open('input.txt')

T = int(input())

def select_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                tem = lst[j]
                lst[j] = lst[i]
                lst[i] = tem

    return lst

for tc in range(1, T + 1):
    num = int(input())
    num_lst = select_sort(list(map(int, input().split())))

    print(f'#{tc} {" ".join([str(x) for x in num_lst])}')

