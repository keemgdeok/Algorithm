select
    ID,
    (case
        when n=1 then "CRITICAL"
        when n=2 then "HIGH"
        when n=3 then "MEDIUM"
        else "LOW"
     end
    ) as COLONY_NAME
from
    (
    select
        id as ID,
        ntile(4) over (order by size_of_colony desc) as n
    from
        ECOLI_DATA
    ) ranked
order by
    ID asc