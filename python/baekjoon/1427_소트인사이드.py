# 숫자를 문자열 그대로 이용해서 소트하고 출력
N = list(input())
N.sort(reverse=True)
print(''.join(N))
