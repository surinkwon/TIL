'''
영어 단어 끝말잇기에서 가장 빨리 탈락하는 사람의 번호와 그 사람의 차례를 출력하는 문제
'''

def solution(n, words):
    answer = [0, 0]
    turn = 1
    cnt_word_last_letter = words[0][-1]
    words_already_spoken = {words[0]}

    while turn < len(words):
        if words[turn][0] != cnt_word_last_letter or words[turn] in words_already_spoken:
            answer = [turn % n + 1, turn // n + 1]
            break
            
        words_already_spoken.add(words[turn])
        cnt_word_last_letter = words[turn][-1]
        turn += 1
    
    return answer