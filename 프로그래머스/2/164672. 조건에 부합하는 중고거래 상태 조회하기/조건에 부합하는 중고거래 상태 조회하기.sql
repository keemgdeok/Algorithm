SELECT
    BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    (case 
        when STATUS = 'SALE' THEN '판매중'
        when STATUS = 'RESERVED' THEN '예약중'
        when STATUS = 'DONE' THEN '거래완료'
    end
    ) as STATUS
from 
    used_goods_board
where
    date_format(created_date, '%Y-%m-%d') = '2022-10-05'
order by
    board_id desc