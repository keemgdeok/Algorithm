select
    ins.name as NAME,
    ins.datetime as DATETIME
from
    ANIMAL_INS ins
left join
    ANIMAL_OUTS outs
    on ins.animal_id = outs.animal_id
where
    outs.animal_id is null
order by
    ins.datetime asc
limit 3