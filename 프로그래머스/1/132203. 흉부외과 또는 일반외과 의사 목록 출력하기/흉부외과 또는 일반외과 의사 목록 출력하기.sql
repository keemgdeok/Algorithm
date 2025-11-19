select
    dr_name as DR_NAME,
    dr_id as DR_ID,
    mcdp_cd as MCDP_CD,
    date_format(hire_ymd, '%Y-%m-%d') as HIRE_YMD
from
    doctor
where
    mcdp_cd = 'CS' or
    mcdp_cd = 'GS'
order by
    hire_ymd desc,
    dr_name asc