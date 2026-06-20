SELECT teachers.name AS teacher, students.name AS students, ROUND(AVG(grade), 1) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE teachers.id = 4 AND students.id = 25
GROUP BY teachers.id;