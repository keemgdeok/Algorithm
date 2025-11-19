select
    a.rest_id as REST_ID,
    a.rest_name as REST_NAME,
    a.food_type as FOOD_TYPE,
    a.favorites as FAVORITES,
    a.address as ADDRESS,
    round(avg(b.review_score), 2) as score
from
    rest_info as a
    join rest_review as b
    on a.rest_id = b.rest_id
where
    address like '서울%'
group by
    a.rest_id
order by
    avg(b.review_score) desc,
    a.favorites desc

    
