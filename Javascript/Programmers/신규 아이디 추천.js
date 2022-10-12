function solution(new_id) {
  var answer = '';
  new_id = new_id.toLowerCase()
  
  // 소문자, 숫자, -, _, .빼고 삭제
  for (i = 0; i < new_id.length; i += 1) {
      if ((97 <= new_id.charCodeAt(i) && new_id.charCodeAt(i) <= 122) || new_id[i] === '-' || new_id[i] === '_' || (48 <= new_id.charCodeAt(i) && new_id.charCodeAt(i) <= 57) || new_id[i] === '.') {
          answer += new_id[i]
      }
  }
  
  // .이 연속으로 있으면 하나만 남기기
  let tmp = ''
  
  for (i = 0; i < answer.length; i += 1) {
      if (answer[i] === '.' && ((i < answer.length - 1 && answer[i + 1] !== '.') || i === answer.length - 1)) {
          tmp += answer[i]
      } else if (answer[i] !== '.') {
          tmp += answer[i]
      }
  }
  
  answer = tmp
  
  // .이 처음이나 마지막에 있으면 삭제
  if (answer[0] === '.') {
      answer = answer.slice(1)
  }
  
  if (answer[answer.length - 1] === '.') {
      answer = answer.slice(0, answer.length - 1)
  }
  
  // 빈 문자열이면 a 대입
  if (answer.length === 0) {
      answer += 'a'
  }
  
  // 길이가 16 이상이면 15개만 남기고 삭제 + 마지막이 .이면 .삭제
  if (answer.length > 15) {
      if (answer[14] === '.') {
          answer = answer.slice(0, 14)
      } else {
          answer = answer.slice(0, 15)
      }
  }
  
  // 길이가 2 이하면 길이가 3이 될 때까지 마지막 문자 붙이기
  if (answer.length < 3) {
      while (answer.length < 3) {
          answer += answer[answer.length - 1]
      }
  }
  
  return answer;
}