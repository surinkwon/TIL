/*
reverse() 를 사용하면 원본 배열이 변형됨 따라서 그걸 원하지 않으면
[...원본배열].reverse() 처럼 전개구문을 사용해서 배열을 복사 후 사용하기
*/

function solution(num_list) {
    var answer = [];
    
    // for (i = num_list.length - 1; i > -1; i -= 1) {
    //     answer.push(num_list[i])
    // }
    
    answer = num_list.reverse()
    return answer;
}