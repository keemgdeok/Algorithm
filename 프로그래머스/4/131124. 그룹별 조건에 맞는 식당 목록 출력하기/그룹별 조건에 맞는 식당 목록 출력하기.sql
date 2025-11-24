select
    prof.member_name as MEMBER_NAME,
    rev.review_text as REVIEW_TEXT,
    date_format(rev.review_date,'%Y-%m-%d') as REVIEW_DATE
from
    member_profile as prof
join
    rest_review as rev
    on prof.member_id = rev.member_id
where
    rev.member_id = (
                    select
                        member_id
                    from
                        rest_review
                    group by
                        member_id
                    order by
                        count(*) desc
                    limit 1
                    )
order by
    rev.review_date asc,
    rev.review_text asc
