/*	==================================================
	
    3.8.2 Join Exercises
    
    Ednalyn C. De Dios
    2019-02-21
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

/*
	-- Join Example Database
*/

-- Use the join_example_db. Select all the records from both the users and roles tables.
USE join_example_db;
SHOW TABLES;
DESCRIBE users;
DESCRIBE roles;
SELECT *
	FROM users
	JOIN roles ON users.role_id = roles.id;

-- Use join, left join, and right join to combine results from the users and roles tables
-- as we did in the lesson. Before you run each query, guess the expected number of results.
SELECT *
	FROM users
    LEFT JOIN roles ON users.role_id = roles.id;
SELECT *
	FROM users
    RIGHT JOIN roles ON users.role_id = roles.id;

-- 1. Although not explicitly covered in the lesson, aggregate functions like count can be
-- used with join queries. Use count and the appropriate join type to get a list of roles
-- along with the number of users that has the role. Hint: You will also need to use group
-- by in the query.
SELECT * FROM users;
SELECT * FROM roles;
SELECT roles.id, roles.name, COUNT(users.id) AS num_of_users
	FROM users
    RIGHT JOIN roles ON users.role_id = roles.id
    GROUP BY roles.id, roles.name;

/* 
	-- Employees Database
*/

-- Use the employees database.
USE employees;
SHOW TABLES;

-- 2. Using the example in the Associative Table Joins section as a guide, write a query
-- that shows each department along with the name of the current manager for that department.

-- SELECT CONCAT(e.first_name, ' ', e.last_name) AS full_name, d.dept_name
-- FROM employees AS e
-- JOIN dept_emp AS de
--   ON de.emp_no = e.emp_no
-- JOIN departments AS d
--   ON d.dept_no = de.dept_no
-- WHERE de.to_date = '9999-01-01' AND e.emp_no = 10001;

SELECT d.dept_name, CONCAT(e.first_name,' ',e.last_name)
	FROM departments AS d
    JOIN dept_manager AS dm
		ON dm.dept_no = d.dept_no
	JOIN employees as e
		ON e.emp_no = dm.emp_no
	-- WHERE dm.to_date = '9999-01-01'
    WHERE dm.to_date > NOW()
    ORDER BY dept_name;

--   Department Name    | Department Manager
--  --------------------+--------------------
--   Customer Service   | Yuchang Weedman
--   Development        | Leon DasSarma
--   Finance            | Isamu Legleitner
--   Human Resources    | Karsten Sigstam
--   Marketing          | Vishwani Minakawa
--   Production         | Oscar Ghazalie
--   Quality Management | Dung Pesch
--   Research           | Hilary Kambil
--   Sales              | Hauke Zhang

-- 3. Find the name of all departments currently managed by women.
SELECT d.dept_name, CONCAT(e.first_name,' ',e.last_name)
	FROM departments AS d
    JOIN dept_manager AS dm
		ON dm.dept_no = d.dept_no
	JOIN employees as e
		ON e.emp_no = dm.emp_no
	WHERE dm.to_date = '9999-01-01' AND e.gender = 'F'
    ORDER BY dept_name;

-- Department Name | Manager Name
-- ----------------+-----------------
-- Development     | Leon DasSarma
-- Finance         | Isamu Legleitner
-- Human Resources | Karsetn Sigstam
-- Research        | Hilary Kambil

-- 4. Find the current titles of employees currently working in the Customer Service department.
SELECT t.title, COUNT(t.title)
	FROM titles AS t
    JOIN dept_emp AS de
	ON t.emp_no = de.emp_no
	JOIN departments AS d
    ON d.dept_no = de.dept_no
	WHERE t.to_date = '9999-01-01' AND d.dept_name = 'Customer Service'
	GROUP BY t.title;

-- Title              | Count
-- -------------------+------
-- Assistant Engineer |    68
-- Engineer           |   627
-- Manager            |     1
-- Senior Engineer    |  1790
-- Senior Staff       | 11268
-- Staff              |  3574
-- Technique Leader   |   241



-- 5. Find the current salary of all current managers.
SELECT d.dept_name, e.first_name, e.last_name, s.salary
FROM departments AS d
JOIN dept_manager AS dm
ON d.dept_no = dm.dept_no
JOIN employees AS e
ON dm.emp_no = e.emp_no
JOIN salaries AS s
ON e.emp_no = s.emp_no
WHERE 	s.to_date LIKE '9999-01-01' AND
		dm.to_date LIKE '9999-01-01'
ORDER BY d.dept_name;

-- Department Name    | Name              | Salary
-- -------------------+-------------------+-------
-- Customer Service   | Yuchang Weedman   |  58745
-- Development        | Leon DasSarma     |  74510
-- Finance            | Isamu Legleitner  |  83457
-- Human Resources    | Karsten Sigstam   |  65400
-- Marketing          | Vishwani Minakawa | 106491
-- Production         | Oscar Ghazalie    |  56654
-- Quality Management | Dung Pesch        |  72876
-- Research           | Hilary Kambil     |  79393
-- Sales              | Hauke Zhang       | 101987

-- 6. Find the number of employees in each department.
SELECT 	d.dept_no,
		d.dept_name,
		COUNT(*) AS num_employees
FROM departments AS d
JOIN dept_emp de
ON d.dept_no = de.dept_no
WHERE de.to_date > NOW()
GROUP BY d.dept_name
ORDER BY d.dept_no;


-- +---------+--------------------+---------------+
-- | dept_no | dept_name          | num_employees |
-- +---------+--------------------+---------------+
-- | d001    | Marketing          | 14842         |
-- | d002    | Finance            | 12437         |
-- | d003    | Human Resources    | 12898         |
-- | d004    | Production         | 53304         |
-- | d005    | Development        | 61386         |
-- | d006    | Quality Management | 14546         |e
-- | d007    | Sales              | 37701         |
-- | d008    | Research           | 15441         |
-- | d009    | Customer Service   | 17569         |
-- +---------+--------------------+---------------+

-- 7. Which department has the highest average salary?
SELECT 	d.dept_name,
		AVG(s.salary)
FROM departments AS d
JOIN dept_emp AS de
ON d.dept_no = de.dept_no
JOIN salaries AS s
ON de.emp_no = s.emp_no
WHERE 	de.to_date > NOW() AND
		s.to_date > NOW()
GROUP BY d.dept_name
ORDER BY AVG(s.salary) DESC
LIMIT 1;

-- +-----------+----------------+
-- | dept_name | average_salary |
-- +-----------+----------------+
-- | Sales     | 88852.9695     |
-- +-----------+----------------+

-- 8. Who is the highest paid employee in the Marketing department?
SELECT e.first_name, e.last_name
FROM employees AS e
JOIN dept_emp AS de
ON e.emp_no = de.emp_no
JOIN departments AS d
ON de.dept_no = d.dept_no
JOIN salaries AS s
ON e.emp_no = s.emp_no
WHERE d.dept_name = 'Marketing'
	AND de.to_date > NOW()
    AND s.to_date > NOW()
ORDER BY s.salary DESC
 LIMIT 1;
 
-- +------------+-----------+
-- | first_name | last_name |
-- +------------+-----------+
-- | Akemi      | Warwick   |
-- +------------+-----------+

-- 9. Which current department manager has the highest salary?
SELECT d.dept_name, e.first_name, e.last_name, s.salary
FROM departments AS d
JOIN dept_manager AS dm
ON d.dept_no = dm.dept_no
JOIN employees AS e
ON dm.emp_no = e.emp_no
JOIN salaries AS s
ON e.emp_no = s.emp_no
WHERE 	s.to_date LIKE '9999-01-01' AND
		dm.to_date LIKE '9999-01-01'
ORDER BY s.salary DESC
LIMIT 1;

-- +------------+-----------+--------+-----------+
-- | first_name | last_name | salary | dept_name |
-- +------------+-----------+--------+-----------+
-- | Vishwani   | Minakawa  | 106491 | Marketing |
-- +------------+-----------+--------+-----------+

-- 10. Bonus Find the fnames of all current employees, their department name, and their current manager's name.

SELECT 	CONCAT(e.first_name,' ',e.last_name) AS 'Employee Name',
		d.dept_name AS 'Department Name',
        CONCAT(em.first_name,' ',em.last_name) AS 'Manager Name'
        FROM employees AS e
        JOIN dept_emp AS de
        ON e.emp_no = de.emp_no
        JOIN departments AS d
        ON de.dept_no = d.dept_no
        JOIN dept_manager as dm
        ON d.dept_no = dm.dept_no
        JOIN employees AS em
        ON dm.emp_no = em.emp_no
        WHERE dm.to_date LIKE '9999%'
        ORDER BY dept_name;
	
SELECT CONCAT(all_employees.first_name, ' ', all_employees.last_name) AS 'Employee Name', 
       dept_name AS 'Department Name',
       CONCAT(managers.first_name, ' ', managers.last_name) AS 'Manager Name'
FROM dept_emp
JOIN departments
  ON dept_emp.dept_no = departments.dept_no
JOIN employees AS all_employees
  ON dept_emp.emp_no = all_employees.emp_no
LEFT JOIN dept_manager
ON departments.dept_no = dept_manager.dept_no
LEFT JOIN employees AS managers
  ON dept_manager.emp_no = managers.emp_no
WHERE dept_emp.to_date > NOW()
   AND dept_manager.to_date > NOW()
ORDER BY dept_name;

-- Employee Name | Department Name  |  Manager Name
-- --------------|------------------|-----------------
--  Huan Lortz   | Customer Service | Yuchang Weedman
--  .....





