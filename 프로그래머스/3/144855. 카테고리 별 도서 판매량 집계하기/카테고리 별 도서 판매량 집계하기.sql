select
    b.CATEGORY,
    sum(s.total_sales) as TOTAL_SALES
from
    BOOK as b
join
    (select
        book_id,
        sum(sales) as total_sales
     from
        book_sales
     where
        date_format(sales_date, '%Y-%m') = '2022-01'
     group by
        book_id
    ) as s
    on b.book_id = s.book_id
group by
    b.category
order by
    b.category asc
