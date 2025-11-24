select
    book_id as BOOK_ID,
    author_name as AUTHOR_NAME,
    date_format(published_date, '%Y-%m-%d') as PUBLISHED_DATE
from
    BOOK as a
join
    AUTHOR as b
    on a.author_id = b.author_id
where
    category = '경제'
order by
    published_date asc