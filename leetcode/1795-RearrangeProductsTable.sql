-- Question Link- https://leetcode.com/problems/rearrange-products-table/




-- Combine Queries of Each Column's price, use Union for combination
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL

UNION ALL

SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL

UNION ALL 

SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL
	-- using "UNION ALL" instead of "UNION" significantly speeds up query, all results will not be dupes (separate store prices) and are new columns in the frame so we can forgo the dupe dropping with "UNION ALL"


