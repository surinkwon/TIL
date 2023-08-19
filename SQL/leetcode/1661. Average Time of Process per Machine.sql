-- join시 timestamp로 비교한 것보다 activity_type으로 구분하는 게 더 빠르게 됐다.

select a.machine_id, round(avg(b.timestamp - a.timestamp), 3) processing_time
from Activity a join Activity b
on a.machine_id = b.machine_id and a.process_id = b.process_id and a.activity_type = 'start' and b.activity_type = 'end'
group by a.machine_id