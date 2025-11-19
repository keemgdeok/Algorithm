select
    warehouse_id as WAREHOUSE_ID,
    warehouse_name as WAREHOUSE_NAME,
    address as ADDRESS,
    ifnull(freezer_yn, 'N') as FREEZER_YN
from
    food_warehouse
where
    address like '경기도%'
order by
    warehouse_id asc

    