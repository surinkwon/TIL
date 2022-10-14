/*
문자열의 길이가 4 또는 6인지, 모두 숫자인지를 파악하는 문제
*/

function solution(s) {
  var answer = true;
  let len = 0
  
  for (i = 0; i < s.length; i += 1) {
      len += 1

      // isNaN 함수는 숫자가 아닐 경우 true 반환
      if (isNaN(s[i])) {
          answer = false
          break
      }
  }
  
  if (len !== 4 && len !== 6) {
      answer = false
  }
  
  return answer;
}