/*
  처음 서브 쿼리에 FOOD_TYPE 대신 REST_ID를 넣었을 때는 일식이 나오지 않았다.
  그 이유는 해당 컬럼에서 어떤 값을 정해야 할지 명확히 주어지지 않았기 때문이다.
  FOOD_TYPE은 GROUP BY로 인해, FAVORITES은 MAX 구문으로 인해 어떤 값을 정할지 확실히 주어졌다.
  하지만 REST_ID를 넣는다면 어떤 값을 정하는 지 모르고 아무 값을 임의로 고른다.
  따라서 결과가 제대로 나오지 않은 것이다. GROUP BY를 쓸 때는 이를 유의하자.
*/

SELECT A.FOOD_TYPE, REST_ID, REST_NAME, A.FAVORITES
FROM REST_INFO AS A
JOIN (
    SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES 
    FROM REST_INFO 
    GROUP BY FOOD_TYPE
) AS B ON A.FOOD_TYPE = B.FOOD_TYPE AND A.FAVORITES = B.FAVORITES
ORDER BY FOOD_TYPE DESC