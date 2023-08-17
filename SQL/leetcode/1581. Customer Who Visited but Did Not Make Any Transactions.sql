select customer_id, count(customer_id) - count(transaction_id ) count_no_trans
from Visits left outer join Transactions
on Visits.visit_id = Transactions.visit_id
group by customer_id
having count_no_trans > 0

-- runtime이 빠른 풀이
/*
select customer_id, count(*) count_no_trans
from Visits left outer join Transactions
on Visits.visit_id = Transactions.visit_id
where transaction_id is null
group by customer_id
*/