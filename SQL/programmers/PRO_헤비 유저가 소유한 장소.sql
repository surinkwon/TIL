-- 공간을 두 개 이상 등록한 유저가 등록한 공간을 조회
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID HAVING COUNT(HOST_ID) >= 2
)
ORDER BY ID