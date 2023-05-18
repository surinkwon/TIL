function solution(numbers) {
  const answer = Array(numbers.length).fill(-1)
  
  for (let i = numbers.length - 2; i > -1; i -= 1) {
      for (let j = i + 1; j < numbers.length; j += 1) {
        if (numbers[j] > numbers[i]) {
              // 뒤에 있는 수가 현재 수보다 클 때
              answer[i] = numbers[j]
              break
          } else if (answer[j] > numbers[i]) {
              // 뒤에 있는 수의 뒷 큰수가 현재 수보다 클 때
              answer[i] = answer[j]
              break
          } else if (answer[j] === -1) {
              // 뒷 큰수가 없을때
              break
          }
      }
  }
  
  return answer;
}