/*
다트게임 점수를 계산하는 문제
*/

function solution(dartResult) {
  var answer = 0;
  let score = ''
  let scores = []
  
  // 스코어 계산 후 배열에 추가
  for (i = 0; i < dartResult.length; i += 1) {
      if (!isNaN(dartResult[i])) {
          if (typeof score === 'number') {
              scores.push(score)
              score = ''
          } 
          score += dartResult[i]
      } else if (dartResult[i] === 'S') {
          score = parseInt(score)
      } else if (dartResult[i] === 'D') {
          score = parseInt(score) ** 2
      } else if (dartResult[i] === 'T') {
          score = parseInt(score) ** 3
      } else if (dartResult[i] === '#') {
          score = -score
      } else if (dartResult[i] === '*') {
          score *= 2
          
          if (scores.length > 0) {
              let preScore = scores.pop()
              scores.push(preScore * 2)
          }
      }
  }
  
  // 마지막 점수 배열에 추가
  scores.push(score)
  
  // 점수 합 계산
  for (i = 0; i < scores.length; i += 1) {
      answer += scores[i]
  }
  return answer;
}