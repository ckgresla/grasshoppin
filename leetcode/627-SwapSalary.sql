/* Question Link- https://leetcode.com/problems/swap-salary/ 
	This one is cool because you cannot use a SELECT statement, had no clue that was a thing prior to this */


/*Interesting use of 'bitwise or' operator and ASCII function*/
UPDATE Salary 
SET sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex))


/*Simple an clean way of doing it*/
UPDATE Salary
	SET sex = (CASE WHEN sex='m'
	THEN 'f'
	ELSE 'm'
	END)

