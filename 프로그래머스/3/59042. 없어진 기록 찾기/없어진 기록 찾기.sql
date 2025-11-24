select
    outs.animal_id as ANIMAL_ID,
    outs.name as NAME
from
    animal_ins as ins
right join
    animal_outs as outs
    on ins.animal_id = outs.animal_id
where
    ins.animal_id is null
    