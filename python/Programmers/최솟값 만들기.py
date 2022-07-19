'''
길이가 같은 두 배열의 각 요소들을 뽑아 해당 요소의 곱을 더함
그렇게 누적한 값의 최소를 구하는 문제
곱이 최소가 되게 하려면 가장 큰 수와 가장 작은 수를 곱해야 함 
따라서 정렬을 이용해 풀면 간단
'''
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    for n in range(len(A)):
        answer += A[n] * B[len(B) - n - 1]
    
    return answer