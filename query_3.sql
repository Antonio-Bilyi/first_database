SELECT groups.number AS group_number, ROUND(AVG(grade), 1) AS average_grade, subjects.name AS subject
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON subject_id = subjects.id
WHERE subjects.id = 1
GROUP by group_id;