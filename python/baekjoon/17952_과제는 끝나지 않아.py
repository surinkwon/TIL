N = int(input())

stack = []
total_score = 0
now = 0

for _ in range(N):
    practice = list(map(int, input().split(" ")))
    
    if practice[0]:
        if now:
            stack.append({"score": now["score"], "rest": now["rest"]})

        now = {"score": practice[1], "rest": practice[2]}
    
    if now:
        now["rest"] -= 1

    if now and not now["rest"]:
        total_score += now["score"]
        
        if len(stack):
            now = stack.pop()
        else:
            now = 0

print(total_score)