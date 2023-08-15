select author_id id
from Views
where author_id = viewer_id
group by author_id
order by author_id

/*
  distinct를 사용해서 중복값을 제거해도 된다.
  select distinct author_id
  from ~
*/