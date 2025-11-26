select
    c.ID,
    c.GENOTYPE,
    p.genotype as PARENT_GENOTYPE
from
    ECOLI_DATA as p
join
    ECOLI_DATA as c
    on p.id = c.parent_id
where
    (p.genotype & c.genotype) = p.genotype
order by
    c.ID asc
