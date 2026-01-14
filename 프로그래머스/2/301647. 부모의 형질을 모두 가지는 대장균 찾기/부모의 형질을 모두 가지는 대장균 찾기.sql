select
    b.id as ID,
    b.genotype as GENOTYPE,
    a.genotype as PARENT_GENOTYPE
from
    ECOLI_DATA a
join
    ECOLI_DATA b
    on a.id = b.parent_id
where
    (a.genotype & b.genotype) = a.genotype
order by
    b.id asc