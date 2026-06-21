SELECT students.name AS student, GROUP_CONCAT(DISTINCT subjects.name) AS subject
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
WHERE students.id = 1;