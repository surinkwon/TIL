'''
배열을 i번부터 j번까지 자른 후 정렬한 다음 k번째 수를 찾는 문제
'''

def solution(array, commands):
    answer = []
    
    for command in range(len(commands)):
        i, j, k = commands[command]
        new_array = array[i - 1:j]

        new_array.sort()
        
        answer.append(new_array[k - 1])
        
    return answer