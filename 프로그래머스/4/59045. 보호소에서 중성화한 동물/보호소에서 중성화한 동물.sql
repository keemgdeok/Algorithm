select
    ins.animal_id as ANIMAL_ID,
    ins.animal_type as ANIMAL_TYPE,
    ins.name as NAME
from
    ANIMAL_INS ins
join
    ANIMAL_OUTS outs
    on ins.animal_id = outs.animal_id
where
    ins.sex_upon_intake like "Intact%"
    and
    (outs.sex_upon_outcome like "Spayed%" or
    outs.sex_upon_outcome like "Neutered%")
order by
    ins.animal_id asc
    
