# Write your MySQL query statement below
SELECT Distinct(teacher_id),count(distinct(subject_id))
as cnt from teacher GROUP by teacher_id;

