/* 시간이 다른 사람들에 비해서 오래 걸린다고 나오는데 왜 그런지 모르겠다.
   똑같은 코드도 시간이 다르게 측정되는 걸 보면 약간의 차이 때문에 그런 것 같기도 하다.
   NULL은 연산자를 통한 값 비교를 할 때 대상이 되지 않아 따로 써줘야 한다.
*/

SELECT NAME
FROM Customer
WHERE REFEREE_ID != 2 OR REFEREE_ID IS NULL