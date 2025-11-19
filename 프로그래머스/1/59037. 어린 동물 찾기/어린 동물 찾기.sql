select
    animal_id as ANIMAL_ID,
    name as NAME
from
    animal_ins
where   
    intake_condition != 'Aged'