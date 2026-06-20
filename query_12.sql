SELECT groups.number AS group_number, students.name AS student, subjects.name AS subject, grades.grade AS grade, grades.date AS lesson_date
FROM grades
JOIN students ON grades.student_id = students.id 
JOIN groups ON students.group_id = groups.id 
JOIN subjects ON grades.subject_id = subjects.id
WHERE groups.id = 1
	AND subjects.id = 3
	AND grades.date = (
		SELECT MAX(date) FROM grades WHERE grades.subject_id = 3
	);