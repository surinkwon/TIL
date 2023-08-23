-- 서브쿼리를 이용해 count를 해서 연산에 사용할 수 있다.

select contest_id, round((count(distinct user_id) / (select count(user_id) from Users)) * 100, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id