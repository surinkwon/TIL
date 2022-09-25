'''
문자열
두 문자열이 애너그램인지 확인하는 문제
'''

N = int(input())

for _ in range(N):
    s1, s2 = input().split()

    if len(s1) != len(s2):
        print(f'{s1} & {s2} are NOT anagrams.')
        continue

    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()
    s2_list.sort()

    if s1_list != s2_list:
        print(f'{s1} & {s2} are NOT anagrams.')
        continue

    print(f'{s1} & {s2} are anagrams.')