select 
    animal_id as ANIMAL_ID,
    name as NAME,
    datetime as DATETIME
from
    animal_ins
order by
    name asc,
    datetime desc
    