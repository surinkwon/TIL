function solution(n, s) {
  if (s / n < 1) {
    return [-1];
  }

  const number = Math.floor(s / n);
  const answer = new Array(n).fill(number);
  let rest = s % n;
  let i = n - 1;

  while (rest) {
    answer[i] += 1;
    rest -= 1;
    i = (i + n - 1) % n;
  }

  return answer;
}
