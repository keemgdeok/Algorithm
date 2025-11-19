select
    pt_name as PT_NAME,
    pt_no as PT_NO,
    gend_cd as GEND_CD,
    age as AGE,
    ifnull(tlno, 'NONE') as TLNO
FROM
    patient
where 
    gend_cd = 'W' and
    age <= 12
order by
    age desc,
    pt_name asc