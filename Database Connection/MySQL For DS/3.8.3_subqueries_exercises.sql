USE employees;

-- 1. Find all the employees with the same hire date as employee 101010 using a sub-query.
SELECT * FROM employees
WHERE hire_date IN (
	SELECT hire_date
    FROM employees
    WHERE emp_no = 101010);


-- 2. Find all the titles held by all employees with the first name Aamod.
USE employees; 
SELECT title
FROM titles
WHERE emp_no IN (
	SELECT emp_no
    FROM employees
    WHERE first_name = 'Aamod');

-- 3. How many people in the employees table are no longer working
-- for the company?
SELECT COUNT(*)
FROM employees
WHERE emp_no NOT IN (
	SELECT emp_no
    FROM salaries
    WHERE to_date > NOW()
);


-- 4. Find all the current department managers that are female
SELECT first_name, last_name
FROM employees
WHERE emp_no IN (
	SELECT emp_no
    FROM dept_manager
    WHERE to_date LIKE '9999%'
) AND gender='F';

-- +------------+------------+
-- | first_name | last_name  |
-- +------------+------------+
-- | Isamu      | Legleitner |
-- | Karsten    | Sigstam    |
-- | Leon       | DasSarma   |
-- | Hilary     | Kambil     |
-- +------------+------------+

-- 5. Find all the employees that currently have a higher than average salary.
SELECT e.first_name, e.last_name, s.salary
FROM employees AS e
JOIN salaries AS s
ON e.emp_no = s.emp_no
WHERE salary > (
	SELECT AVG(salary)
	FROM salaries
)
AND s.to_date LIKE '9999%';

-- +------------+-----------+--------+
-- | first_name | last_name | salary |
-- +------------+-----------+--------+
-- | Georgi     | Facello   | 88958  |
-- | Bezalel    | Simmel    | 72527  |
-- | Chirstian  | Koblick   | 74057  |
-- | Kyoichi    | Maliniak  | 94692  |
-- | Tzvetan    | Zielinski | 88070  |
-- +------------+-----------+--------+

-- 6. How many current salaries are within 1 standard deviation of the highest salary??
-- What percentage of all salaries is this?
SELECT COUNT(salary)
FROM salaries
WHERE salary > (
	SELECT MAX(salary)-STD(salary)
	FROM salaries
)
AND to_date LIKE '9999%';

-- 78 / 240,124 = .03%