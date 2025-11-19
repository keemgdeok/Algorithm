select
    factory_id as FACTORY_ID,
    factory_name as FACTORY_NAME,
    address as ADDRESS
from 
    food_factory
where
    address like '강원도%'
order by
    factory_id asc