select
    year(a.differentiation_date) as YEAR,
    (b.max_colony - a.size_of_colony) as YEAR_DEV,
    a.id as ID
from
    ECOLI_DATA a
join
    (
        select
            max(size_of_colony) as max_colony,
            year(DIFFERENTIATION_DATE) as max_year
        from
            ECOLI_DATA
        group by
            year(DIFFERENTIATION_DATE)
    ) b
    on year(a.differentiation_date) = b.max_year
order by
    year(a.differentiation_date) asc,
    YEAR_DEV asc
    
    
