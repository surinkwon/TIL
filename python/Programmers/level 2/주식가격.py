def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        # 현재 주식 가격보다 이전 주식 가격이 클 때까지 주식을 빼고
        # 가격이 떨어지지 않은 기간 설정
        while len(stack) and stack[len(stack) - 1][1] > prices[i]:
            index, price = stack.pop()
            answer[index] = i - index
        
        # 스택에 현재 주식 추가
        stack.append([i, prices[i]])
    
    # 끝까지 남아있는 주식들의 기간 설정
    for i in range(len(stack)):
        index, price = stack[i]
        answer[index] = len(prices) - index - 1
    
    return answer