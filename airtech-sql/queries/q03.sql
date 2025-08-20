SELECT DISTINCT m.*
FROM employees m
JOIN employees e ON e.manager_id = m.employee_id
ORDER BY m.employee_id
