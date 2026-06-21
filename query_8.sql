SELECT teachers.name AS teacher, subjects.name AS subject, ROUND(AVG(grade), 1) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id 
JOIN teachers ON subjects.teacher_id = teachers.id 
WHERE teachers.id = 1;