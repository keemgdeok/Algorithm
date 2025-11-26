select distinct
    dv.id as ID,
    dv.email as EMAIL,
    dv.first_name as FIRST_NAME,
    dv.last_name as LAST_NAME
from
    SKILLCODES as sc
join
    DEVELOPERS as dv
    on (sc.code & dv.skill_code) > 0
where
    sc.name = 'Python' or sc.name = 'C#'
order by
    dv.id asc