'''
주어진 전화번호부에서 어떤 전화번호가 다른 전화번호의 접두사가 되는 경우가 있으면 False
없으면 True를 반환하는 문제
'''

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i][0] == phone_book[j][0] and len(phone_book[i]) < len(phone_book[j]):
                
                for letter in range(0, len(phone_book[i])):
                    if phone_book[i][letter] != phone_book[j][letter]:
                        break

                if letter == len(phone_book[i]) - 1 and phone_book[i][-1] == phone_book[j][len(phone_book[i])-1]:
                    return False
                
            else:
                break
        
    return answer