select
    info.item_id as ITEM_ID,
    info.item_name as ITEM_NAME,
    info.rarity as RARITY
from
    ITEM_INFO info
join
    ITEM_TREE tree
    on info.item_id = tree.item_id
where
    tree.parent_item_id is not null
    and parent_item_id in (
        select
            item_id
        from
            ITEM_INFO
        where
            rarity = "RARE"
    )
order by
    ITEM_ID desc