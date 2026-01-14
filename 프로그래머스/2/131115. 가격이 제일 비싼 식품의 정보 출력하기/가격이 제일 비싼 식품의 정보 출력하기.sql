select
    fp.product_id as PRODUCT_ID,
    fp.product_name as PRODUCT_NAME,
    fp.product_cd as PRODUCT_CD,
    fp.category as CATEGORY,
    fp.price as PRICE
from
    FOOD_PRODUCT fp
where
    (fp.product_id, fp.price) = (
        select
            product_id,
            price
        from 
            FOOD_PRODUCT
        order by
            price desc
        limit 1
    )