select distinct
    d.id as ID,
    d.email as EMAIL,
    d.first_name as FIRST_NAME,
    d.last_name as LAST_NAME
from
    skillcodes s
join
    developers d
    on (s.code & d.skill_code) > 0 
where
    s.category = "Front End"
order by
    d.id asc
