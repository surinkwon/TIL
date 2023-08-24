-- case when을 통해 count에 조건을 걸 수 있다.

select query_name, round(avg(rating / position), 2) as quality, round((count(case when rating < 3 then 1 end) / count(*)) * 100, 2) as poor_query_percentage
from Queries
group by query_name