select
    fh.flavor as FLAVOR
from
    first_half as fh
join
    ( 
    select
        flavor,
        sum(total_order) as total_order
    from
        july
    group by
        flavor
    ) as jy
    on fh.flavor = jy.flavor
order by
    fh.total_order + jy.total_order desc
limit 3;
    