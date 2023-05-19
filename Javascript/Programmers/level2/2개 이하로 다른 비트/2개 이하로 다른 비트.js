function solution(numbers) {
  const answer = [];
  
  for (const number of numbers) {
      // 이진수 변환
      const numberStringList = Array.from(number.toString(2))

      // 가장 오른쪽 '0'비트 찾기
      let mostRightZeroIndex = 0
      for (let i = 1; i < numberStringList.length; i += 1) {
          if (numberStringList[i] === '0') {
              mostRightZeroIndex = i
          }
      }
      
      // 가장 오른쪽 '0' 비트가 맨 뒤에 있으면서 1이 아닐 때
      if (mostRightZeroIndex === numberStringList.length - 1 && number !== 1) {
          numberStringList[numberStringList.length - 1] = '1'
      } 
      // '0' 비트가 없을 때
      else if (mostRightZeroIndex === 0) {
          numberStringList[0] = '0'
          numberStringList.unshift('1')  
      } else {
          numberStringList[mostRightZeroIndex] = '1'
          numberStringList[mostRightZeroIndex + 1] = '0'
      }
      
      // 2진수를 10진수로 변환
      answer.push(parseInt(numberStringList.join(''), 2))
  }
  
  return answer;
}