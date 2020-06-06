--Ů�Ծ�ס�طֲ�
select area, count(area) from data1
group by area

--��ż��ѡ��ס��
select sarea,count(sarea) from data1
group by sarea

--Ů������ˮƽ
select salary,count(salary) from data1 where salary is not null
group by salary

--Ů��ְҵְλ
select professional_position,count(professional_position)from data2 where professional_position != '--'
group by professional_position

--Ů��רҵ
select major,count(major)from data1 where major is not null
group by major

--Ů�Ի���״���ķֲ�
select marry,count(marry)cnt from data1 where marry is not null
group by marry

--��ͬŮ�Ի���״�������Ի���״����Ҫ��
select smarriage,count(smarriage) cnt from data1 where smarriage is not null
and marry='����'
group by smarriage

--Ů��ѧ���ֲ����
select education,count(education)from data1 where education is not null
group by education

--��ͬѧ��Ů�Զ�����ѧ��Ҫ��
select seducation,count(seducation)from data1 where seducation is not null
and education=''
group by seducation

--δ��Ⱥ�����ѧ���ֲ�
select education,count(education) cnt from data1
where marry='δ��'
group by education 

--ѧ�����Ƿ�ҪС��
select a.child,b.education,count(b.education) cnt
from data1 a,data1 b
where a.child is not null and b.education is not null
	 and a.name=b.name
group by a.child,b.education

--Ů��ѧ��������������ѧ��
select a.education,b.seducation,count(a.education) cnt from data1 a,data1 b
where a.name=b.name
group by b.seducation,a.education

--Ů������ֲ�
SELECT
    nld AS '����ֲ�',
    count(*) AS '����'
FROM
    (
        SELECT
            CASE

        WHEN age >= 21
        AND age <= 30 THEN
            '21-30'
        WHEN age >= 31
        AND age <= 40 THEN
            '31-40'
		WHEN age >= 41
        AND age <= 50 THEN
            '41-50'
		WHEN age >= 51
        AND age <= 60 THEN
            '51-60'
		WHEN age >= 61
		THEN '61����'
        END AS nld
        FROM
            data1
    ) a
GROUP BY
    nld
order by nld

--�Ⱥ�ϰ��
--smoke
select moke, count(moke) from data1 where moke is  not null
group by moke
--drink
select drink, count(drink) from data1 where drink is  not null
group by drink
--exercise
select exercise, count(exercise) from data1 where exercise is  not null
group by exercise
--eating_habits
select eating_habits, count(eating_habits) from data1 where eating_habits is  not null
group by eating_habits
--shopping
select shopping, count(shopping) from data1 where shopping is  not null
group by shopping
--sleep
select sleep, count(sleep) from data1 where sleep is  not null
group by sleep
--social
select social, count(social) from data1 where social is  not null
group by social
--child
select child, count(child) from data1 where child is  not null
group by child
--marry_time
select marry_time, count(marry_time) from data1 where marry_time is  not null 
group by marry_time