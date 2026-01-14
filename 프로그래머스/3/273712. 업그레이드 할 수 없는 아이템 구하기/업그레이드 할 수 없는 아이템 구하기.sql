select distinct
    info.item_id as ITEM_ID,
    info.item_name as ITEM_NAME,
    info.rarity as RARITY
from
    ITEM_INFO info
left join
    ITEM_TREE tree
    on info.item_id = tree.parent_item_id
where
    tree.parent_item_id is null
order by
    info.item_id desc
    