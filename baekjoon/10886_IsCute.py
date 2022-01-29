# 0 = not cute / 1 = cute
pn = int(input())

cute = not_cute = 0

for _ in range(pn):
    vote = int(input())

    if vote == 1:
        cute += 1
    else:
        not_cute += 1

if cute > not_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')