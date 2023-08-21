-- count 내부에서도 distinct를 사용할 수 있다.

select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id