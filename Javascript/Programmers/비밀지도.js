/*
이진수 변환을 통해 비밀 지도를 만들고 출력하는 문제
*/

// 2진수 변환 함수
function binary(n, len) {
  let rlt = ''
  
  while (n > 0) {
      rlt = String(n % 2) + rlt
      n = parseInt(n / 2)
  }
  
  while (rlt.length < len) {
      rlt = '0' + rlt
  }
  
  return rlt
}

function solution(n, arr1, arr2) {
  var answer = [];
  
  
  for (i = 0; i < n; i += 1) {
      let tmp = ''
      
      // 2진수 변환
      const first = binary(arr1[i], n)
      const second = binary(arr2[i], n)
      
      // 두 지도 비교
      for (j = 0; j < n; j += 1) {
          if (first[j] === '1' || second[j] === '1') {
              tmp += '#'
          } else {
              tmp += ' '
          }
      }
      
      // 지도 복원
      answer.push(tmp)
  }
  
  return answer;
}