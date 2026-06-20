SELECT students.name AS student, ROUND(AVG(grades.grade), 1) AS average_grade, subjects.name AS subject
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subject_id = 2
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;