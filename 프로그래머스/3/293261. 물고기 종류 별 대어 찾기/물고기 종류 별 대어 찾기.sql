select
    info.id as ID,
    name.fish_name as FISH_NAME,
    info.length as LENGTH
from
    FISH_INFO info
join
    FISH_NAME_INFO name
    on info.fish_type = name.fish_type
where
    (info.fish_type, info.length) in (
        select
            fish_type,
            max(length)
        from
            FISH_INFO
        group by
            fish_type
    )
order by
    info.id asc
    