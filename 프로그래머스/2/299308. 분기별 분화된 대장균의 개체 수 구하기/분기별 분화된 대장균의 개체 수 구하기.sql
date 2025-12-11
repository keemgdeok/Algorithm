select
    ed.quarter as QUARTER,
    count(*) as ECOLI_COUNT
from
    (select 
        *,
        (case
            when month(DIFFERENTIATION_DATE) < 4 then "1Q"
            when month(DIFFERENTIATION_DATE) < 7 then "2Q"
            when month(DIFFERENTIATION_DATE) < 10 then "3Q"
            else "4Q"
         end
        ) as QUARTER
    from
        ECOLI_DATA
    ) as ed
group by
    quarter
order by
    quarter asc