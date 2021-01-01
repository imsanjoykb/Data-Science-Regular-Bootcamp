USE employees;
DESCRIBE employees;
DESCRIBE departments;

USE ada_678;

/* Using the example from the lesson, re-create the employees_with_departments table. */

CREATE TEMPORARY TABLE employees_with_departments AS
SELECT emp_no, first_name, last_name, dept_no, dept_name
FROM employees.employees
JOIN employees.dept_emp USING(emp_no)
JOIN employees.departments USING(dept_no)
LIMIT 100;

-- Add a column named full_name to this table. It should be a VARCHAR whose
-- length is the sum of the lengths of the first name and last name columns
ALTER TABLE employees_with_departments ADD full_name VARCHAR(30);

-- Update the table so that full name column contains the correct data
UPDATE employees_with_departments
SET full_name = CONCAT(first_name, ' ', last_name);

-- Remove the first_name and last_name columns from the table.
ALTER TABLE employees_with_departments DROP COLUMN first_name;
ALTER TABLE employees_with_departments DROP COLUMN last_name;

-- What is another way you could have ended up with this same table?
-- IDK

/* Create a temporary table based on the payments table from the sakila database. */
USE sakila;
SHOW TABLES;
DESCRIBE payment;

USE ada_678;

CREATE TEMPORARY TABLE this_payment AS
SELECT customer_id, staff_id, rental_id, amount, payment_date, last_update
FROM sakila.payment;

-- Write the SQL necessary to transform the amount column such that it is stored as
-- an integer representing the number of cents of the payment. For example, 1.99
-- should become 199.
#UPDATE this_payment SET amount = CAST((amount * 10) AS INT);
UPDATE this_payment SET amount = amount * 10;

/* Find out how the average pay in each department compares to the overall average pay.
In order to make the comparison easier, you should use the Z-score for salaries. In terms
of salary, what is the best department to work for? The worst? */
USE employees;

SELECT AVG(salary) from salaries WHERE to_date LIKE '9999%';
-- 72012.2359

SELECT STD(salary) from salaries;
-- 16904.82828800014

SELECT a.dept_name, AVG(a.z_salary) AS avg_z_salary
FROM  (
	SELECT d.dept_name,
		s.emp_no,
        s.salary,
        ((s.salary-(SELECT AVG(salary) FROM employees.salaries WHERE to_date > NOW())
		)  / (SELECT STDDEV(salary)  FROM employees.salaries WHERE to_date > NOW())
        ) AS z_salary
	FROM employees.salaries AS s
	JOIN employees.dept_emp de
    ON s.emp_no = de.emp_no
	JOIN departments AS d
    ON de.dept_no = d.dept_no
	WHERE s.to_date > NOW()
	) AS a
GROUP BY a.dept_name;

