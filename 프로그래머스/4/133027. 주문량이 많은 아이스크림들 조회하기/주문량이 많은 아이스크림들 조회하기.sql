select
    FLAVOR
from
    (
    select
        SHIPMENT_ID,
        FLAVOR,
        TOTAL_ORDER
    from
        first_half
    union all
    select
        SHIPMENT_ID,
        FLAVOR,
        TOTAL_ORDER
    from
        july
    ) a
group by
    flavor
order by
    sum(total_order) desc
limit 3