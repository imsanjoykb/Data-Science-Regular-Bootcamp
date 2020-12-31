/*	==================================================
	
    3.7 Group By Exercises
    
    Ednalyn C. De Dios
    2019-02-20
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

-- 1. Use the GROUP BY clause to create more complex queries
USE employees;

-- 2. In your script, use DISTINCT to find the unique titles in the titles table.
SELECT DISTINCT(title) FROM titles;

-- 3. Update the query find just the unique last names that start and end
-- with 'E' using GROUP BY.
SELECT last_name FROM employees
WHERE last_name LIKE 'e%' AND last_name LIKE '%e' 
GROUP BY last_name;

-- 4. Update your previous query to now find unique combinations of first and
-- last name where the last name starts and ends with 'E'.
SELECT first_name, last_name FROM employees
WHERE last_name LIKE 'e%' AND last_name LIKE '%e' 
GROUP BY first_name, last_name;

-- 5. Find the unique last names with a 'q' but not 'qu'.
SELECT last_name FROM employees
WHERE last_name LIKE '%q%' AND last_name NOT LIKE '%qu%'
GROUP BY last_name;

-- 6. Which (across all employees) name is the most common?
SELECT first_name, COUNT(*) FROM employees
GROUP BY first_name
ORDER BY COUNT(first_name) DESC
LIMIT 1;

SELECT last_name, COUNT(*) FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC
LIMIT 1;

-- 6. Which (across all employees) name is the least common? 
SELECT first_name, COUNT(*) FROM employees
GROUP BY first_name
ORDER BY COUNT(first_name)
LIMIT 1;

SELECT last_name, COUNT(*) FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name)
LIMIT 1;
 
-- 6. COMBO
SELECT CONCAT(first_name,' ',last_name), COUNT(CONCAT(first_name,' ',last_name))
FROM employees
GROUP BY CONCAT(first_name,' ',last_name)
ORDER BY COUNT(CONCAT(first_name,' ',last_name)) DESC, CONCAT(first_name,' ',last_name) ASC;

SELECT CONCAT(first_name,' ',last_name), COUNT(CONCAT(first_name,' ',last_name))
FROM employees
GROUP BY CONCAT(first_name,' ',last_name)
ORDER BY COUNT(CONCAT(first_name,' ',last_name)) ASC, CONCAT(first_name,' ',last_name) ASC;


-- 7. Update your query for 'Irena', 'Vidya', or 'Maya'. Use COUNT(*)
-- and GROUP BY to find the number of employees for each gender
-- with those names.
SELECT COUNT(gender),gender FROM employees
WHERE first_name IN ('Irena', 'Vidya', 'Maya' )
GROUP BY gender;

-- 8. Recall the query the generated usernames for the employees from
-- the last lesson. Are there any duplicate usernames?
SELECT COUNT(DISTINCT(
	LOWER(CONCAT(
	SUBSTR(first_name,1,1),
	SUBSTR(last_name,1,4),
    '_',
    SUBSTR(birth_date,6,2),
    SUBSTR(birth_date,3,2)))))
FROM employees;

SELECT 
    LOWER(CONCAT(SUBSTR(first_name, 1, 1),
                    SUBSTR(last_name, 1, 4),
                    '_',
                    SUBSTR(birth_date, 6, 2),
                    SUBSTR(birth_date, 3, 2))),
    COUNT(LOWER(CONCAT(SUBSTR(first_name, 1, 1),
                    SUBSTR(last_name, 1, 4),
                    '_',
                    SUBSTR(birth_date, 6, 2),
                    SUBSTR(birth_date, 3, 2))))
FROM
    employees
GROUP BY (LOWER(CONCAT(SUBSTR(first_name, 1, 1),
                SUBSTR(last_name, 1, 4),
                '_',
                SUBSTR(birth_date, 6, 2),
                SUBSTR(birth_date, 3, 2))))
	

-- Bonus: how many duplicate usernames are there?
-- 300,024 - 282,737 = 17,287 (last four of last name)
-- 300,024 - 285,872 = 14,152 (first four of last name)





