/*
  행 간의 차이를 어떻게 구할지 몰랐는데, 문제 카테고리가 basic join이라고 되어 있어서 self join으로 풀어야겠다고 생각했다.
  DATEDIFF를 사용하면 앞 날짜 - 뒷 날짜로 동작한다. 따라서 앞 날짜를 기준으로 비교했다.
  self join을 할 때는 alias를 사용하자.
*/

select a.id
from Weather a join Weather b
on datediff(a.recordDate, b.recordDate) = 1
where a.temperature > b.temperature