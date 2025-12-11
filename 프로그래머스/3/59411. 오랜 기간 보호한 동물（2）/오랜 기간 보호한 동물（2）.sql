select
    ins.animal_id as ANIMAL_ID,
    ins.name as NAME
from
    ANIMAL_INS as ins
join    
    ANIMAL_OUTS as outs
    on ins.animal_id = outs.animal_id
order by
    outs.datetime - ins.datetime desc
limit 2;