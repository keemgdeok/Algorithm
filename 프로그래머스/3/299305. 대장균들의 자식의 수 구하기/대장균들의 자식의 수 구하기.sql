select
    p.ID,
    ifnull(count(c.id),0) as CHILD_COUNT
from
    ECOLI_DATA as p
left join 
    ECOLI_DATA as c
    on p.ID = c.parent_id
group by
    p.ID