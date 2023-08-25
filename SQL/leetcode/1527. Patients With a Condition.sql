-- 접두사가 DIAB1이여야 하기 때문에 앞에 뭐가 더 붙어있으면 안 됨
-- > 앞에 한 번 띄워줘야 한다.
select *
from Patients
where conditions like '% DIAB1%' or conditions like 'DIAB1%'