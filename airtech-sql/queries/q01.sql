SELECT e.*
FROM employees e
LEFT JOIN countries c ON e.country_id = c.country_id
ORDER BY c.country_name, e.employee_id
