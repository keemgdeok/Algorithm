select
    ID,
    case
        when n = 1 then "CRITICAL"
        when n = 2 then "HIGH"
        when n = 3 then "MEDIUM"
        ELSE "LOW"
    end as COLONY_NAME
from
    (
    select
        ID,
        ntile(4) over (order by size_of_colony desc) as n
    from ecoli_data
    ) as ranked
order by
    id asc