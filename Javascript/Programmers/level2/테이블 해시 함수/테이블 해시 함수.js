function solution(data, col, row_begin, row_end) {
    // 계산을 편하게 하기 위한 전처리
    col -= 1
    data.unshift(0)
    
    // 정렬
    data.sort((a, b) => {
        if (a[col] === b[col]) {
            return b[0] - a[0]
        }
        
        return a[col] - b[col]
    })
    
    // S_i 구하기
    const si = []
    
    for (let i = row_begin; i <= row_end; i += 1) {
        let sum = 0
        for (const value of data[i]) {
            sum += value % i
        }
        
        si.push(sum)
    }
    
    // 누적 XOR
    let answer = si[0]

    for (let i = 1; i < si.length; i += 1) {
        answer = answer ^ si[i]
    }
    
    return answer
}