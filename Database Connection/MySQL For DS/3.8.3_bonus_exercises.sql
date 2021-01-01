
-- 1. Find all the department names that currently have female managers.
SELECT dept_name
FROM departments
WHERE dept_no IN (
	SELECT dept_no
    FROM dept_manager
    WHERE emp_no IN (
		SELECT emp_no
        FROM employees
        WHERE gender = 'F'
    ) AND to_date > NOW()
);


-- +-----------------+
-- | dept_name       |
-- +-----------------+
-- | Development     |
-- | Finance         |
-- | Human Resources |
-- | Research        |
-- +-----------------+

-- 2. Find the first and last name of the employee with the highest salary.

SELECT first_name, last_name
FROM employees
WHERE emp_no = (
	SELECT emp_no
	FROM salaries
	WHERE salary = (
		SELECT MAX(salary)
		FROM salaries
	)
);

SELECT first_name, last_name
FROM employees
WHERE emp_no = (
	SELECT emp_no
	FROM salaries
	ORDER BY salary DESC
	LIMIT 1
);

-- +------------+-----------+
-- | first_name | last_name |
-- +------------+-----------+
-- | Tokuyasu   | Pesch     |
-- +------------+-----------+

-- 3. Find the department name that the employee with the highest salary works in.

SELECT dept_name
FROM departments
WHERE dept_no = (
	SELECT dept_no
	FROM dept_emp
	WHERE emp_no = (
		SELECT emp_no
		FROM employees
		WHERE emp_no = (
			SELECT emp_no
			FROM salaries
			ORDER BY salary DESC
			LIMIT 1
		)
	)
);

-- +-----------+
-- | dept_name |
-- +-----------+
-- | Sales     |
-- +-----------+
