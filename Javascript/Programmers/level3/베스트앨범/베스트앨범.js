function solution(genres, plays) {
    let answer = []
    const totalPlayNum = {}
    const includedNum = {}
    
    // 장르별 총 플레이 횟수 저장
    for (let i = 0; i < genres.length; i += 1) {
        if (totalPlayNum[genres[i]]) {
            totalPlayNum[genres[i]] += plays[i]
        } else {
            totalPlayNum[genres[i]] = plays[i]
        }
        
        includedNum[genres[i]] = 0
        genres[i] = [genres[i], plays[i], i]
    }
    
    // 기준에 따라 노래 정렬
    genres.sort((a, b) => {
        // 장르가 같을 때
        if (a[0] === b[0]) {
            // 장르가 같으면서 플레이 횟수도 같을 때 노래 번호대로 오름차순 정렬
            if (a[1] === b[1]) {
                return a[2] - b[2]
            }
            
            // 플레이 횟수대로 내림차순 정렬
            return b[1] - a[1]
        }
        
        // 총 플레이 횟수가 많은 장르 순으로 정렬
        return totalPlayNum[b[0]] - totalPlayNum[a[0]]
    })
    
    // 앨범에 노래 추가
    for (const song of genres) {
        const genre = song[0]
        const songNum = song[2]
        
        if (includedNum[genre] < 2) {
            answer.push(songNum)
            includedNum[genre] += 1
        }
    }
    
    return answer
}