import sys

S, E, Q = input().split()
S = list(map(int, S.split(':')))    # 총회 시작 시간
E = list(map(int, E.split(':')))    # 총회 끝나는 시간
Q = list(map(int, Q.split(':')))    # 스트리밍 끝나는 시간

attendance = {}
rlt = 0

while True:
    try:
        chat_time, nickname = sys.stdin.readline().split()
        chat_hour, chat_minute = list(map(int, chat_time.split(':')))

        # 입장 확인
        if chat_hour < S[0] or (chat_hour == S[0] and chat_minute <= S[1]):
            attendance[nickname] = 'attend'

        # 퇴장 확인
        else:

            # 입장 했으면
            if attendance.get(nickname):

                # 채팅 기록이 총회 끝나는 시간 후이면서
                if chat_hour > E[0] or (chat_hour == E[0] and chat_minute >= E[1]):

                    # 스트리밍 끝나는 시간 전이면 퇴장 확인
                    if chat_hour < Q[0] or (chat_hour == Q[0] and chat_minute <= Q[1]):
                        attendance[nickname] = 0
                        rlt += 1
    except:
        print(rlt)
        break