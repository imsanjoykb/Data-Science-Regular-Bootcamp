/*	==================================================
	
    3.3 Tables Exercises
    
    Ednalyn C. De Dios
    2019-02-19
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

USE employees;
	-- use the employees db
    
SHOW TABLES;
	-- list all tables

DESCRIBE employees;
	-- explore the employees table
    -- int, date, varchar, and enum

SHOW TABLES;
	-- numeric: dept_emp, salaries
    -- string: departments, dept_manager, employees, titles 
    -- date: dept_emp, deprt_emp_latest_date

DESCRIBE departments;
	-- relationship: departments can have many employees
    
SHOW CREATE TABLE dept_manager;
	-- show SQL that created dept_manager table
    /*
    CREATE TABLE `dept_manager` (
		`emp_no` int(11) NOT NULL,
		`dept_no` char(4) NOT NULL,
		`from_date` date NOT NULL,
		`to_date` date NOT NULL,
		PRIMARY KEY (`emp_no`,`dept_no`),
		KEY `dept_no` (`dept_no`),
		CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,
		CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) REFERENCES `departments` (`dept_no`) ON DELETE CASCADE
	) ENGINE=InnoDB DEFAULT CHARSET=latin1 */
    



