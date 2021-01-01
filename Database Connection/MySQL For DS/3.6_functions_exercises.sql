/*	==================================================
	
    3.6 Function Exercises
    
    Ednalyn C. De Dios
    2019-02-20
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

-- 1. Copy the order by exercise and save it as 3.6_functions_exercises.sql.

USE employees;

-- 2. Update your queries for employees whose names start and end with 'E'.
-- Use concat() to combine their first and last name together as a single
-- column named full_name.
SELECT CONCAT(first_name,' ',last_name) AS full_name
FROM employees
WHERE last_name LIKE 'e%' AND last_name LIKE '%e'
ORDER BY emp_no;

-- 3. Convert the names produced in your last query to all uppercase.
SELECT UPPER(CONCAT(first_name,' ',last_name)) AS full_name
FROM employees
WHERE last_name LIKE 'e%' AND last_name LIKE '%e'
ORDER BY emp_no;

-- 4. For your query of employees born on Christmas and hired in the 90s,
-- use datediff() to find how many days they have been working at the company
-- (Hint: You will also need to use NOW() or CURDATE())
SELECT 
	first_name,
    last_name,
    hire_date,
    DATEDIFF(NOW(),hire_date) AS days_working_for_company,
    ROUND(DATEDIFF(NOW(),hire_date)/365.25,1) AS years_working_for_company
FROM employees
WHERE 	birth_date LIKE '____-12-25' AND 
		(hire_date  BETWEEN '1990/01/01' AND
        '1999/12/31')
ORDER BY ROUND(DATEDIFF(NOW(),hire_date)/365.25,1) DESC
LIMIT 10;

-- 5. Find the smallest and largest salary from the salaries table.
SELECT * FROM salaries
ORDER BY salary
LIMIT 1;

SELECT * FROM salaries
ORDER BY salary DESC
LIMIT 1;

SELECT MIN(salary), MAX(salary)
FROM salaries;


-- 6. Use your knowledge of built in SQL functions to generate a username
-- for all of the employees. A username should be all lowercase, and consist
-- of the first character of the employees first name, the first 4 characters
-- of the employees last name, an underscore, the month the employee was born,
-- and the last two digits of the year that they were born.

SELECT LOWER(CONCAT(
	SUBSTR(first_name,1,1),
	SUBSTR(last_name,1,4),
    '_',
    SUBSTR(birth_date,6,2),
    SUBSTR(birth_date,3,2)))
FROM employees;



