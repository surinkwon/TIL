function solution(storey) {
    let answer = 0
    
    while (storey > 0) {
        
        // 가장 아랫자리 층
        const floor = storey % 10

        // 아랫자리 층이 5를 넘어가면 올라간다
        if (floor > 5) {
            answer += 10 - floor
            storey += 10
        } else {

            // 아랫자리 층이 5일 때 그 윗자리 층이 5 이상이면 올라간다
            if (floor === 5 && parseInt(storey / 10) % 10 >= 5) {
                storey += 10
            }

            // 그렇지 않은 경우 내려간다
            answer += storey % 10
        }

        storey = parseInt(storey / 10)
    }
    
    return answer
}