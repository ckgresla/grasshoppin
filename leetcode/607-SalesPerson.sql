-- Question Link- https://leetcode.com/problems/sales-person/




-- Use a Subquery to find all sales_id that are associated with Companies named RED, then select the SalesPerson names of all not in that col
SELECT SP.name
FROM SalesPerson SP 
WHERE SP.sales_id NOT IN 
	(SELECT O.sales_id
	 FROM Orders O
	 LEFT JOIN Company C on O.com_id = C.com_id
	 WHERE C.name = "RED")
	

-- 
SELECT SP.name 
FROM Orders O JOIN Company C 
	ON O.com_id = C.com_id AND C.name="RED"
RIGHT JOIN SalesPerson SP ON O.sales_id = SP.sales_id
WHERE O.sales_id IS NULL; 

