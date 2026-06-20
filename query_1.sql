SELECT students.name AS student, ROUND(AVG(grade), 1) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY students.name
ORDER BY AVG(grade) DESC 
LIMIT 5;