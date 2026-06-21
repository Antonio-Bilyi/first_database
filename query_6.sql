SELECT students.name AS student, groups.number AS group_number
FROM students
JOIN groups ON students.group_id = groups.id
WHERE group_id = 1;