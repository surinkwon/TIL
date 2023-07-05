'''
처음에는 
for i in range(2, int(number)):
        if number % i == 0:
            return 0
위와 같이 짜서 시간초과가 되었다.
그 다음에는 에라토스테네스의 체를 사용해서 구현했는데 
백만 아래의 숫자 중 2진수로 변환하면 자릿수가 10자리가 넘어가는 숫자가 생겨서 메모리 에러가 났다.
소수인지 판별할 때 해당 수의 루트인 수까지만 검사하면 된다는 것을 알게되고 사용하니 풀렸다.
'''

# 소수인지 판별하는 함수
def isPrime(number):
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return 0
    return 1

def solution(n, k):
    num = ''                                # n을 k진수로 변환한 값을 담을 변수
    while n > 0:                            # k진수로 변환
        num = str(n%k) + num
        n //= k
    
    nums = []
    nn = ''
    for i in range(len(num)):               # k진수로 변환한 값에서 숫자를 추출
        if num[i] != '0':                   # 0이 아닌 숫자면 임시 문자열에 +
            nn += num[i]
        else:                               # 0이면 임시 문자열을 정수로 바꿔서 nums에 추가
            if nn:
                nums.append(int(nn))
            nn = ''
    
    if nn:                                  # 마지막에 0이 없을 시 숫자 하나가 추가가 안 되므로 이를 처리
        nums.append(int(nn))
    
        
    answer = 0
    
    for num in range(len(nums)):
        if nums[num] != 1:
            answer += isPrime(nums[num])    # 각 숫자가 소수인지 판별하고 개수 셈
            
    return answer