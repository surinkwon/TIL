# 유클리드 호제법 사용
# 최대공약수 구하는 함수
def lcmF(num1, num2):
    while num1 % num2 != 0:
        rest = num1 % num2
        num1 = num2
        num2 = rest
    
    return num2

def gcfF(num1, num2, lcm):
    return lcm * (num1 // lcm) * (num2 // lcm)


N, M = map(int, input().split())
lg = max(N, M)
sm = min(N, M)

lcm = lcmF(lg, sm)
gcf = gcfF(lg, sm, lcm)

print(lcm)
print(gcf)