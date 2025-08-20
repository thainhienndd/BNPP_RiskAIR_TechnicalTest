SELECT *
FROM employees
WHERE manager_id IS NOT NULL
ORDER BY employee_id
