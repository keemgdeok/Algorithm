select
    p.product_code as PRODUCT_CODE,
    (p.price * s.total_amount) as SALES
from
    product p
join
    (
        select
            product_id,
            sum(sales_amount) as total_amount
        from
            offline_sale
        group by
            product_id
    ) s
    on p.product_id = s.product_id
order by
    SALES desc,
    PRODUCT_CODE asc
    