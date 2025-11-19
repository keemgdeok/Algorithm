select
    id as ID,
    email as EMAIL,
    first_name as FIRST_NAME,
    last_name as LAST_NAME
from
    developer_infos
where
    skill_1 = 'Python' or
    skill_2 = 'Python' or
    skill_3 = 'Python'
order by
    id asc