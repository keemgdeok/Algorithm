select
    p.member_name as MEMBER_NAME,
    r.review_text as REVIEW_TEXT,
    date_format(r.review_date, '%Y-%m-%d') as REVIEW_DATE
from
    member_profile p
join
    rest_review r
    on p.member_id = r.member_id
where
    r.member_id = (
        select
            member_id
        from
            rest_review
        group by
            member_id
        order by
            count(member_id) desc
        limit 1
    )
order by
    REVIEW_DATE asc,
    REVIEW_TEXT asc