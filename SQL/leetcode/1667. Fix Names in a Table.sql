-- +로는 문자열을 이어붙일 수 없다. concat 함수를 쓰자.

select user_id, concat(upper(left(name, 1)), lower(right(name, length(name) - 1))) as name
from Users
order by user_id