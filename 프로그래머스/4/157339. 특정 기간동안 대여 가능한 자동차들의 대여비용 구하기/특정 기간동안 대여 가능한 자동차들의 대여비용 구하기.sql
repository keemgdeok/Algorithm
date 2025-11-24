select
    car.car_id as CAR_ID,
    car.car_type as CAR_TYPE,
    floor(car.daily_fee * 30 * (100 - plan.discount_rate ) / 100) as FEE
from
    CAR_RENTAL_COMPANY_CAR as car
join
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan
    on car.car_type = plan.car_type and
    plan.duration_type = '30일 이상'
where
    car.car_type in ('세단', 'SUV')
    and not exists (
        select 1
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY hist
        where hist.car_id = car.car_id
            and hist.start_date <= '2022-11-30'
            and hist.end_date >= '2022-11-01'
    )
    and floor(
        car.daily_fee * 30 * (100 - plan.discount_rate) / 100
    ) between 500000 and 1999999
order by
    fee desc,
    car.car_type asc,
    car.car_id desc