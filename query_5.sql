SELECT teachers.name AS teacher, subjects.name AS subject 
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = 1;