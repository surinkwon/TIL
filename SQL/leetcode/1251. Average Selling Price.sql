-- 단순히 avg로 해서는 결과가 제대로 나오지 않는다.

select p.product_id, round(sum(p.price * u.units) / sum(u.units), 2) average_price
from Prices p join UnitsSold u
on p.product_id = u.product_id and p.start_date <= u.purchase_date and u.purchase_date <= p.end_date
group by p.product_id