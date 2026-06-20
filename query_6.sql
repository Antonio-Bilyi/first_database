SELECT students.name AS student, groups.number AS group_number
FROM students
JOIN groups ON students.group_id = groups.id
ORDER BY groups.id;