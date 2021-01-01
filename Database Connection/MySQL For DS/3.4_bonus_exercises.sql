/*	==================================================
	
    3.4 Bonus Exercises
    
    Ednalyn C. De Dios
    2019-02-19
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/


/*
Write a query that shows all the information in the `help_topic` table in the
	`mysql` database. How could you write a query to search for a specific help
	topic?
 */
SELECT * FROM mysql.help_topic;

/*
Take a look at the information in the salaries table in the employees
	database. What do you notice?
*/
USE `sakila`;

/*
Explore the `sakila` database. What do you think this database represents?
	What kind of company might be using this database?
 */
SHOW TABLES;

/*
Write a query that shows all the columns from the `actors` table
*/
SELECT * FROM `actor`;

/*
write a query that only shows the last name of the actors from the 
 `	actors` table
*/
SELECT `last_name` FROM `actor`;

/*
Write a query that displays the title, description, rating, movie length
	columns from the `films` table for films that last 3 hours or longer.
*/
SELECT 	`title`,
		`description`, 
        `rating`,
        `length`
FROM `film`
WHERE `length` > 180;

/*
Select the payment id, amount, and payment date columns from the payments
     table for payments made on or after 05/27/2005.
*/
SELECT 	`payment_id`,
		`amount`,
        `payment_date`
FROM `payment`
WHERE `payment_date` >= '05/27/2005';

/*
Select the primary key, amount, and payment date columns from the payment
     table for payments made on 05/27/2005.
*/
SELECT 	`payment_id`,
		`amount`,
		`payment_date`
FROM `payment`
WHERE `payment_date` = '05/27/2005';