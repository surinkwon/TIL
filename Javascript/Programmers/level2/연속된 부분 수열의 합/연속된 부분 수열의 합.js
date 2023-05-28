function solution(sequence, k) {
    const answer = [sequence.length, 0]
    let minLength = sequence.length
    let sum = sequence[0]
    let [start, end] = [0, 0]
    
    while (end < sequence.length) {
        if (sum < k) {

            // 부분수열의 합이 k보다 작으면 수열의 길이를 늘림
            end += 1
            if (end < sequence.length) {
                sum += sequence[end]
            }
        } else if (sum > k) {

            // 부분수열의 합이 k보다 크면 수열의 길이를 줄임
            sum -= sequence[start]
            start += 1
        } else {
            
            // 부분수열의 합이 k이면 이전 답의 길이와 비교
            if (end - start + 1 < minLength || (end - start + 1 === minLength && answer[0] > start)) {
                answer[0] = start
                answer[1] = end
                minLength = end - start + 1
            }
            
            sum -= sequence[start]
            start += 1
        }
    }
    
    return answer
}