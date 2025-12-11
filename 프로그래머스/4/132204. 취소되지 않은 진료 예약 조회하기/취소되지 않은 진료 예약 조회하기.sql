select
    a.apnt_no as APNT_NO,
    p.pt_name as PY_NAME,
    a.pt_no as PT_NO,
    a.mcdp_cd as MCDP_CD,
    d.dr_name as DR_NAME,
    a.apnt_ymd as APNT_YMD
from
    appointment as a
join
    patient as p
    on a.pt_no = p.pt_no
join 
    doctor as d
    on a.mddr_id = d.dr_id
where
    date_format(a.apnt_ymd, "%Y-%m-%d") = "2022-04-13" and
    a.apnt_cncl_yn = "N" and
    a.mcdp_cd = "CS"
order by
    a.apnt_ymd asc
