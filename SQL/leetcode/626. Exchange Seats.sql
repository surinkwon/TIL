-- join을 하지 않고 그냥 id 조작으로도 풀 수 있다. (case when 등으로)
select t1.id as id, if (t1.id % 2 = 1, if (t3.id is null, t1.student, t3.student), t2.student) as student
from Seat t1 left outer join Seat t2
on t1.id = t2.id + 1
left outer join Seat t3
on t1.id + 1 = t3.id
order by id