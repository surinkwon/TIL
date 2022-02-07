# 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == 0:
        break

    if a <= b:
        if b % a:
            print('neither')
        else:
            print('factor')
    else:
        if a % b:
            print('neither')
        else:
            print('multiple')