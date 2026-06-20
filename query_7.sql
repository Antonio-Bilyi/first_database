SELECT groups.number AS group_number, students.name AS student, grades.grade AS grade, subjects.name AS subject
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.id = 1 AND groups.id = 2;