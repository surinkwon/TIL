-- 2019-07-27일 까지의 기록을 보는 거기 때문에 0보다 같거나 크다는 조건도 넣어줘야 한다.

select date_format(activity_date, '%Y-%m-%d') as day, count(distinct user_id) as active_users
from Activity
where datediff('2019-07-27', activity_date) < 30 and datediff('2019-07-27', activity_date) >= 0
group by activity_date