/**
 * 시작 시간과 과제하는 데 걸리는 시간을 받아 끝나는 시간을 계산하는 함수
 * @param {number} start 시작 시간
 * @param {number} playtime 과제 하는 데 걸리는 시간
 * @returns 끝나는 시간과 분을 반환
 */
function calEnd(start, playtime) {
    let hour = start[0]
    let minute = start[1] + playtime
    
    if (minute >= 60) {
        hour += parseInt(minute / 60)
        minute %= 60
    }
    
    return [hour, minute]
}

/**
 * 두 시간 데이터의 차이가 몇 분인지 계산하는 함수
 * @param {number[]} end 끝나는 시간(더 이후의 시간)
 * @param {number[]} start 시작 시간(더 이전의 시간)
 * @returns 두 시간 데이터의 차이를 분으로 반환
 */
function calRestTime(end, start) {
    const [endHour, endMinute] = end
    const [startHour, startMinute] = start
    let hour = endHour - startHour
    let minute = endMinute - startMinute
    let rest = 0
    
    if (minute < 0) {
        hour -= 1
        minute += 60
    }
    
    rest += hour * 60 + minute
    
    return rest
    
}

function solution(plans) {
    const answer = []
    const waiting = []
    
    // 시작 시간을 숫자로 변환
    // 끝나는 시간을 계산해 추가
    for (let i = 0; i < plans.length; i += 1) {
        const plan = plans[i]
        const start = plan[1].split(':').map(e => Number(e))
        plan[1] = start
        plan[2] = Number(plan[2])
        plan.push(calEnd(start, plans[i][2]))
        
        plans[i] = plan
    }
    
    // 시작 시간이 빠른 순으로 정렬
    plans.sort((a, b) => {
        if (a[1][0] === b[1][0]) {
            return a[1][1] - b[1][1]
        }
        
        return a[1][0] - b[1][0]
    })
    
    for (let i = 0; i < plans.length - 1; i += 1) {
        const cs = plans[i]
        const ns = plans[i + 1]
        const csEnd = cs[3]
        const nsStart = ns[1]
        
        if (csEnd[0] > nsStart[0] || (csEnd[0] === nsStart[0] && csEnd[1] > nsStart[1])) {
            // 이후 과제보다 지금 하고있는 과제가 늦게 끝날 경우
            // 남은 시간을 계산해서 대기 줄에 추가
            waiting.push([cs[0], calRestTime(csEnd, nsStart)])

        } else {
            // 현재 과제를 끝내고 다음 과제까지 시간이 남은 경우 원래 하던 과제를 함
            answer.push(cs[0])
            let restTime = calRestTime(nsStart, csEnd)
            
            if (waiting.length) {
                let ws = waiting[waiting.length - 1]
                
                while (waiting.length && ws[1] <= restTime) {
                    answer.push(ws[0])
                    restTime -= ws[1]
                    
                    waiting.pop()
                    ws = waiting[waiting.length - 1]
                }
                
                // 남은 시간동안 원래 하던 과제를 끝내지 못하면 남은 시간동안만 함
                if (restTime && waiting.length) {
                    waiting[waiting.length - 1][1] -= restTime
                }
            }
            
        }
    }
    
    // 마지막 과제를 끝낸 후 이전에 하던 과제들을 모두 끝냄
    answer.push(plans[plans.length - 1][0])
    
    for (let i = waiting.length - 1; i > -1; i -= 1) {
        answer.push(waiting[i][0])
    }
    
    return answer
}