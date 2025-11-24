select
    a.product_code as PRODUCT_CODE,
    a.price*b.sales_amount as SALES
from
    product as a
join
    (
        select 
            product_id,
            sum(sales_amount) as sales_amount
        from 
            offline_sale
        group by
            product_id
    ) as b
    on a.product_id = b.product_id
order by
    sales desc,
    a.product_code asc