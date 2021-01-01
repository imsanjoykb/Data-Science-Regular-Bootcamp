/*	==================================================
	
    3.4 Select Exercises
    
    Ednalyn C. De Dios
    2019-02-19
    
    MySQL
    Ada Cohort
    Codeup Data Science Career Accelerator Program

	==================================================
*/

USE albums_db;
SHOW TABLES;

SELECT * FROM albums WHERE artist = "Pink Floyd";
	-- The name of all albums by Pink Floyd

SELECT release_date FROM albums WHERE `name` = "Sgt. Pepper's Lonely Hearts Club Band";
	-- The year Sgt. Pepper's Lonely Hearts Club Band was released

SELECT genre FROM albums WHERE `name` = "Nevermind";
	-- The genre for the album Nevermind

SELECT * FROM albums WHERE release_date BETWEEN 1990 and 1999;
	-- Which albums were released in the 1990s

SELECT * FROM albums WHERE sales < 20;
	-- Which albums had less than 20 million certified sales

SELECT * FROM albums WHERE genre = "Rock";
	-- All the albums with a genre of "Rock"
    -- "Rock" doesn't match the texts "Hard rock" and "Progressive rock"

SELECT * FROM albums WHERE genre LIKE '%rock%'
	-- '%rock%' matches the texts "Hard rock" and "Progressive rock"





