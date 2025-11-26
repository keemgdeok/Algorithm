select
    info.ITEM_ID,
    info.ITEM_NAME,
    info.RARITY
from
    ITEM_INFO as info
join
    ITEM_TREE as tree
    on info.item_id = tree.item_id
where
    parent_item_id in (select
                        item_id
                       from
                        item_info
                       where
                        rarity = 'RARE'
                      )
order by
    info.item_id desc