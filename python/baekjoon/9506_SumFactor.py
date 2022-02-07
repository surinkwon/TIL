# 약수들의 합
while True:
    num = int(input())
    total = 0
    if num == -1:
        break
    
    factor = [str(i) for i in range(1, num) if num % i == 0]

    for number in factor:
        total += int(number)
    
    if total == num:
        print(f'{num} = {" + ".join(factor)}')
    else:
        print(f'{num} is NOT perfect.')
    
    


