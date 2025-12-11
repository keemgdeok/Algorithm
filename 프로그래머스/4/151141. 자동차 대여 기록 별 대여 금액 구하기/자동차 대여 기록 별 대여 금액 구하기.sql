select
    h.history_id as HISTORY_ID,
    round(c.daily_fee * (datediff(h.end_date, h.start_date) + 1) * (100 - ifnull(discount_rate, 0)) / 100, 0)
    
    as FEE
from
    CAR_RENTAL_COMPANY_CAR as c
join
    CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    on c.car_id = h.car_id
left join
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on c.car_type = p.car_type and
    p.duration_type  = (case
                            when datediff(h.end_date, h.start_date) + 1 >= 90 then "90일 이상"
                            when datediff(h.end_date, h.start_date) + 1 >= 30 then "30일 이상"
                            when datediff(h.end_date, h.start_date) + 1>= 7 then "7일 이상"
                            else null
                        end              
                      )
where 
    c.car_type = "트럭"
order by 
    fee desc,
    h.history_id desc
    
    

    