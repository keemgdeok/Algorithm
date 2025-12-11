select
    ANIMAL_ID,
    NAME,
    (case
        when sex_upon_intake like "%Neutered%" then "O"
        when sex_upon_intake like "%Spayed%" then "O"
     else "X"
     end
    ) as "중성화"
from
    ANIMAL_INS
    