/*
영어로 된 숫자를 수로 변환해 원래 수를 반환하는 문제
*/

function solution(s) {
  var answer = '';
  
  const numbers = {
      'one': '1',
      'two': '2',
      'three': '3',
      'four': '4',
      'five': '5',
      'six': '6',
      'seven': '7',
      'eight': '8',
      'nine': '9',
      'zero': '0'
  }
  
  let word = ''
  
  for (i = 0; i < s.length; i += 1) {
      if (!isNaN(s[i])) {
          if (word in numbers) {
              answer += numbers[word]
              word = ''
          }
          answer += s[i]
      } else {
          
          if (word in numbers) {
              answer += numbers[word]
              word = ''
          }
          
          word += s[i]
      }
  }
  
  if (word) {
      answer += numbers[word]
  }
  
  return parseInt(answer);
}