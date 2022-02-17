import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    laser = input()

    # 막대 개수, 총 막대 개수
    now_stick = total_stick = i = 0

    while i < len(laser):

        # 여는 괄호를 만나면 막대 개수 + 1 (레이저가 아닐 때)
        if laser[i] == '(' and laser[i+1] != ')':
            now_stick += 1
            i += 1
    
        # 레이저를 만나면 여태까지 있던 막대 개수 * 2 를 총 막대 개수에 더해줌
        elif laser[i] == '(' and laser[i + 1] == ')':
            total_stick += now_stick
            i += 2
        elif laser[i] == ')' and laser[i - 1] != '(': 
            now_stick -= 1                            # 닫는 괄호를 만나면 막대 개수 -1
            total_stick += 1                          # 레이저로 막대기를 나눌 때 나눠진 막대기의 개수는 더해주지 않았으므로 닫는 괄호를 만나면 이를 더해줌
            i += 1

    print(f'#{tc} {total_stick}')

