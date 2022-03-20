# 2부터 나눠가며 나머지가 0이 나오면 그만둠
N = int(input())
numbers = list(map(int, input().split()))
total = len(numbers)

for i in range(len(numbers)):
    for n in range(2, numbers[i]):
        if numbers[i] % n == 0:
            total -= 1
            break

if 1 in numbers:
    total -= 1

print(total)