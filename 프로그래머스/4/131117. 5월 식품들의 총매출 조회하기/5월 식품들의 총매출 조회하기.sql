select
    o.product_id as PRODUCT_ID,
    p.product_name as PRODUCT_NAME,
    (p.price * o.total_amount) as TOTAL_SALES
from
    FOOD_PRODUCT p
join
    (
    select
        product_id,
        sum(amount) as total_amount
    from
        FOOD_ORDER
    where
        date_format(produce_date, '%Y-%m') = '2022-05'
    group by
        product_id
    ) o 
    on p.product_id = o.product_id
order by
    TOTAL_SALES desc,
    PRODUCT_ID asc
    
    