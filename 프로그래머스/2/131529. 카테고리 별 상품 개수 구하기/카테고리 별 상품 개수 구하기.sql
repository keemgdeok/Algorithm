select
    left(product_code, 2) as CATEGORY,
    count(*) as PRODUCT
from
    product
group by
    CATEGORY
order by
    CATEGORY asc