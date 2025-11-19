select
    a.item_id as ITEM_ID,
    a.item_name as ITEM_NAME
from
    item_info as a
join
    item_tree as b
    on a.item_id = b.item_id
where
    b.parent_item_id is null
