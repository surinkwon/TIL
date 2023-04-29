function solution(name, yearning, photo) {
  const answer = [];
  const yearningScore = {}
  
  // 각 이름의 그리움 점수를 객체에 저장
  for (let i = 0; i < name.length; i += 1) {
      yearningScore[name[i]] = yearning[i]
  }
  
  // 각 사진의 추억 점수 계산
  for (const photoNames of photo) {
      let score = 0
      for (const photoName of photoNames) {
          score += yearningScore[photoName] ? yearningScore[photoName] : 0
      }
      answer.push(score)
  }
  
  return answer;
}