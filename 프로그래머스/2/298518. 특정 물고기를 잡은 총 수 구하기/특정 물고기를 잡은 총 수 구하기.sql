select
    count(*) as FISH_COUNT
from
    FISH_INFO as info
join
    FISH_NAME_INFO as name
    on info.fish_type = name.fish_type
where
    name.fish_name in ('BASS', 'SNAPPER')