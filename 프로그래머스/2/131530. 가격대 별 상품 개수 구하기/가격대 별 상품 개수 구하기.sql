select
    truncate(price / 10000, 0) * 10000 as PRICE_GROUP,
    count(*) as PRODUCTS
from
    product
group by
    PRICE_GROUP
order by
    PRICE_GROUP asc