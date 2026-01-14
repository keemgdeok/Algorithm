select
    outs.animal_id as ANIMAL_ID,
    outs.name as NAME
from
    ANIMAL_INS ins
right join
    ANIMAL_OUTS outs
    on ins.animal_id = outs.animal_id
where
    ins.animal_id is null
