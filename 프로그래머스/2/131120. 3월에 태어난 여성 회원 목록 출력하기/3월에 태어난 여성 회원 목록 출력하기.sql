select
    member_id as MEMBER_ID,
    member_name as MEMBER_NAME,
    gender as GENDER,
    date_format(date_of_birth, '%Y-%m-%d') as DATE_OF_BIRTH
from
    member_profile
where
    gender = 'W' and
    month(date_of_birth) = 3 and
    tlno is not null
order by
    member_id asc