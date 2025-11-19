select
    YEAR(a.differentiation_date) as YEAR,
    (b.max_size - a.size_of_colony) as YEAR_DEV,
    A.ID
from
    ecoli_data as a
    join (
        select 
            year(differentiation_date) as YEAR,
            max(size_of_colony) as max_size
        from ecoli_data
        group by
            year(differentiation_date)
    ) as b
    on year(a.differentiation_date) = b.YEAR
order by
    YEAR asc,
    YEAR_DEV asc
    