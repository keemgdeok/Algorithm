select
    ins.animal_id as ANIMAL_ID,
    ins.animal_type as ANIMAL_TYPE,
    ins.name as NAME
from
    animal_ins ins
join
    animal_outs outs
    on ins.animal_id = outs.animal_id
where
    ins.sex_upon_intake like 'Intact%'
    and outs.sex_upon_outcome not like 'Intact%'
order by
    ANIMAL_ID asc