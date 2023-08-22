-- 다른 풀이를 참고하면 join하는 것보다 서브쿼리 써서 not in 하는 게 더 빠르다.

select t1.employee_id
from Employees t1 left outer join Employees t2
on t1.manager_id  = t2.employee_id
where t1.manager_id is not null and t2.employee_id is null and t1.salary < 30000
order by t1.employee_id