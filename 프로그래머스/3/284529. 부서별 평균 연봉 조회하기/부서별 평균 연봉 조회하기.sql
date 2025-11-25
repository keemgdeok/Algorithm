select
    dep.DEPT_ID,
    dep.DEPT_NAME_EN,
    round(avg(emp.sal), 0) as AVG_SAL
from
    HR_DEPARTMENT as dep
join
    HR_EMPLOYEES as emp
    on dep.dept_id = emp.dept_id
group by
    emp.dept_id
order by
    AVG_SAL desc
    