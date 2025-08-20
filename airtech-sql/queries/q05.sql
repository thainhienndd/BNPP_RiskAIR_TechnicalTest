SELECT e.*, m.first_name AS mgr_first, m.last_name AS mgr_last
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id