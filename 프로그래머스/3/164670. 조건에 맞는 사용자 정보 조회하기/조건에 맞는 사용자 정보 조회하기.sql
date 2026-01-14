select
    u.user_id as USER_ID,
    u.nickname as NICKNAME,
    concat(u.city, " ", u.street_address1, " ", u.street_address2) as 전체주소,
    concat(substr(u.tlno,1,3), "-", substr(u.tlno,4,4), "-", substr(u.tlno,8,4)) as 전화번호
from
    USED_GOODS_BOARD b
join
    USED_GOODS_USER u
    on b.writer_id = u.user_id
group by
    b.writer_id
having
    count(*) >= 3
order by
    USER_ID desc
