def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    index = 0

    while n > 0 and works[index]:
        while index < len(works) - 1 and works[index] == works[index + 1]:
            index += 1

        if index < len(works) - 1:
            need = works[index] - works[index + 1]
        elif index == len(works) - 1:
            need = works[index]
        else:
            need = n
        
        if need * (index + 1) <= n:
            for i in range(index + 1):
                works[i] -= need
                n -= need
            
            while index < len(works) - 1 and works[index] == works[index + 1]:
                index += 1
        else:
            value = n // (index + 1)
            for i in range(index + 1):
                works[i] -= value
                n -= value
            
            for i in range(index + 1):
                if n <= 0 or not works[index]:
                    break

                works[i] -= 1
                n -= 1
    
    for i in range(len(works)):
        answer += works[i] ** 2

    return answer