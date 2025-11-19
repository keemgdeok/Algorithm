select
    b.ingredient_type as INGREDIENT_TYPE,
    sum(total_order) as TOTAL_ORDER
from
    first_half as a
join
    icecream_info as b
    on a.flavor = b.flavor
group by
    ingredient_type

    




    