select 
    distinct
    dp.id as ID,
    dp.email as EMAIL,
    dp.first_name as FIRST_NAME,
    dp.last_name as LAST_NAME
from
    skillcodes as sc
join
    developers as dp
    on dp.skill_code & sc.code > 0
where 
    sc.category = "Front End"
order by
    dp.id asc
    