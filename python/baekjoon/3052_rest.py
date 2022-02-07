'''
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
# 리스트 생성하고 값을 받아 저장
number = []

for _ in range(10):
    number.append(int(input()))

# 리스트 원소를 42로 나누고 나머지 저장
for num in range(len(number)):
    number[num] = number[num] % 42

# 나머지를 정렬
fin = 0
stor = 0
for fsr in range(len(number)):
    for scd in range(len(number)):
        if number[fsr] > number[scd]:
            stor = number[fsr]
            number[fsr] = number[scd]
            number[scd] = stor

for index in range(9):
        if number[index] != number[index + 1]:
            fin += 1

print(fin + 1)