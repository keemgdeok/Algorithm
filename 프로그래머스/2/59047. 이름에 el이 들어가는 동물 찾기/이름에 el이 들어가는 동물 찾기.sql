select
    ANIMAL_ID,
    NAME
from
    ANIMAL_INS
where
    animal_type = 'Dog' and
    name like '%el%'
order by
    name asc
