SELECT c.country_name, c.region, COUNT(e.employee_id) AS nb_employees
FROM countries c
LEFT JOIN employees e ON e.country_id = c.country_id
GROUP BY c.country_name, c.region
ORDER BY nb_employees DESC