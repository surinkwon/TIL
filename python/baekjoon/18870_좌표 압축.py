N = int(input())

numbers = list(map(int, input().split()))
tmp = sorted(list(set(numbers)))
num_dict = {}

for i in range(len(tmp)):
    num_dict[tmp[i]] = i

for i in range(len(numbers)):
    print(num_dict[numbers[i]], end=' ')


