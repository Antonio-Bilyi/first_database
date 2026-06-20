SELECT DISTINCT teachers.name AS teacher, subjects.name AS subjects, students.name AS student
FROM grades
JOIN subjects ON grades.subject_id = subjects.id 
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE teachers.id = 1 AND students.id = 2;