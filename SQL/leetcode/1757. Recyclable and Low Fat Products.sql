-- select low_fat and recyclable products
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'