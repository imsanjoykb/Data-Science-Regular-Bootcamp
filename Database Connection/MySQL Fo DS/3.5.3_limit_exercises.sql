/*	==================================================
	
    3.5.3 Limit Exercises
    
    Ednalyn C. De Dios
    2019-02-20
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

USE employees;

/* 	2. MySQL provides a way to return only unique results from our queries with the
	keyword DISTINCT. For example, to find all the unique titles within the company,
    we could run the following query:
	
    SELECT DISTINCT title FROM titles;
    
	List the first 10 distinct last name sorted in descending order. 
*/
SELECT DISTINCT last_name FROM employees
ORDER BY last_name
LIMIT 10;

/*	
    3. Find your query for employees born on Christmas and hired in the 90s from
    order_by_exercises.sql. Update it to find just the first 5 employees.
*/
SELECT * FROM employees
WHERE birth_date LIKE '____-12-25' AND 
	(hire_date  BETWEEN '1990/01/01' AND '1999/12/31')
ORDER BY birth_date, hire_date DESC
LIMIT 5;

/*
	4. Try to think of your results as batches, sets, or pages. The first five results
    are your first page. The five after that would be your second page, etc. Update
    the query to find the tenth page of results.
*/
SELECT * FROM employees
WHERE birth_date LIKE '____-12-25' AND 
	(hire_date  BETWEEN '1990/01/01' AND '1999/12/31')
ORDER BY birth_date, hire_date DESC
LIMIT 5 OFFSET 45;

/*
	LIMIT and OFFSET can be used to create multiple pages of data. What is the
    relationship between OFFSET (number of results to skip), LIMIT (number of results
    per page), and the page number?
    
    (PAGE-1)/LIMIT=OFFSET
    
*/
