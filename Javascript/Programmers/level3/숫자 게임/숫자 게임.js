function solution(A, B) {
    let answer = 0
    let [ai, bi] = [0, 0]
    
    // 내림차순 정렬
    A.sort((a, b) => b - a)
    B.sort((a, b) => b - a)
    
    while (ai < A.length) {
        if (B[bi] > A[ai]) {
            answer += 1
            bi += 1
        }
        
        ai += 1
    }
    
    return answer
}