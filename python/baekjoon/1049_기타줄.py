N, M = map(int, input().split())

packages = [0] * M
indis = [0] * M

# 6줄 패키지와 낱개별 가격 리스트
for i in range(len(packages)):
    package, indi = map(int, input().split())
    packages[i] = package
    indis[i] = indi

# total1은 낱개 6개 사는 것보다 패키지 하나 사는 것이 더 싸면서
# 6줄씩을 모두 사고 남은 나머지 개수에 대해서는 더 적은 금액으로 살 수 있는
# 상황을 계산
total1 = (N // 6) * min(packages)

if min(indis) * (N % 6) > min(packages):
    total1 += min(packages)
else:
    total1 += min(indis) * (N % 6)

# total2는 가장 적은 금액의 패키지로 모두 사는 경우
# total3은 가장 적은 낱개 금액으로 모두 사는 경우
total2 = (N // 6 + 1) * min(packages)
total3 = N * min(indis)

print(min(total1, total2, total3))
    
