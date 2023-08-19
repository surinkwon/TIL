-- select 할 때 어떤 테이블인지 적어주면 빠르다.

select Employee.name, Bonus.bonus
from Employee left outer join Bonus
on Employee.empId = Bonus.empId
where bonus < 1000 or bonus is null