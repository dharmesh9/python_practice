-- Q1. What is the total number of orders in the dataset?
SELECT count(*) as total_orers 
FROM t1;

-- Q2. How many unique customers made purchases?
SELECT count( customer_id ) as total_unique_customer 
FROM t1;

-- Q3. What is the total revenue generated?
SELECT SUM(purchase_amount) AS total_revenue 
FROM t1;

-- Q4. What is the average purchase amount?
SELECT AVG(purchase_amount) AS avg_revenue 
FROM t1;

-- Q5. What are the unique product categories?
SELECT DISTINCT category  
FROM t1;

-- Q6. Which products are purchased the most?
SELECT item_purchased, count(item_purchased) as total_purchased
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q7. Which colors are most frequently purchased?
SELECT color, count(color) as total_purchased
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q8. Which sizes are most frequently purchased?
SELECT size, count(size)  as total_purchased
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q9. Which seasons have the highest number of orders?
SELECT season, count(season)  as total_purchased
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q10. Which seasons generate the most revenue?
SELECT season, SUM(purchase_amount) as total_revenue
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q11. Which locations generate the most orders?
SELECT location, count(purchase_amount) as total_orders
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q12. Which locations generate the most revenue?
SELECT location, sum(purchase_amount) as total_revenue
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q13. What is the gender distribution of customers?
SELECT gender, COUNT(customer_id)  AS gender_distribution
FROM t1
GROUP BY 1;

-- Q14. What is the age distribution of customers?
SELECT age, COUNT(customer_id)  AS age_distribution
FROM t1
GROUP BY 1
ORDER BY 1;

-- Q15. What is the average review rating across all products?
SELECT ROUND(AVG(review_rating), 2) AS avg_review_rating
FROM t1;

-- Q16. Which products have the highest average rating?
SELECT item_purchased, ROUND(AVG(review_rating),2) AS highest_avg_rating
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q17. Which products have the lowest average rating?
SELECT item_purchased, ROUND(AVG(review_rating),2) AS lowest_avg_review_rating
FROM t1
GROUP BY 1
ORDER BY 2 ASC;

-- Q18. Which categories have the highest average rating?
SELECT category, ROUND(AVG(review_rating),2) AS highesst_avg_review_rating
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q19. Which categories generate the most revenue?
SELECT category, SUM(purchase_amount) AS total_revenue
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q20. Which categories generate the most orders?
SELECT category, count(*) AS total_orders
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q21. Which customers have made the highest number of purchases?
SELECT customer_id,
       COUNT(*) AS total_orders
FROM t1
GROUP BY customer_id
ORDER BY total_orders DESC;

-- Q22. Which customers have spent the most money overall (CLV)?
SELECT customer_id,
       SUM(purchase_amount) AS total_spent
FROM t1
GROUP BY customer_id
ORDER BY total_spent DESC;

-- Q23. Which customers have the highest average order value?
SELECT customer_id,
       ROUND(AVG(purchase_amount), 2) AS avg_order_value
FROM t1
GROUP BY customer_id
ORDER BY avg_order_value DESC;

-- Q24. Which customers buy the widest variety of categories?
SELECT customer_id,
       COUNT(DISTINCT category) AS unique_categories
FROM t1
GROUP BY customer_id
ORDER BY unique_categories DESC;

-- Q25. Which customers buy the widest variety of products?
SELECT customer_id, COUNT(DISTINCT item_purchased) AS unique_products
FROM t1
GROUP BY customer_id
ORDER BY unique_products DESC;

-- Q26. Which customers buy the widest variety of colors?
SELECT customer_id, COUNT(DISTINCT color) AS unique_colors
FROM t1
GROUP BY customer_id
ORDER BY unique_colors DESC;

-- Q27. Which customers buy the widest variety of sizes?
SELECT customer_id, COUNT(DISTINCT size) AS unique_sizes
FROM t1
GROUP BY customer_id
ORDER BY unique_sizes DESC;

-- Q28. Which customers always use discounts?
SELECT customer_id, discount_applied
FROM t1
WHERE discount_applied = 'Yes' or 'YES';

-- Q29. Which customers never use discounts?
SELECT customer_id, discount_applied
FROM t1
WHERE discount_applied = 'No' or 'NO';

-- Q30. Which customers give the highest average ratings?
SELECT customer_id, ROUND(AVG(CAST(review_rating AS DECIMAL(5,2))),2) AS highest_avg_rating
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- SELECT *
-- FROM t1
-- WHERE `review_rating` IS NULL
--    OR `review_rating` NOT REGEXP '^[0-9]+(\\.[0-9]+)?$';

SET SQL_SAFE_UPDATES = 0;
UPDATE t1
SET review_rating = CASE category
    WHEN 'Clothing' THEN 3.1
    WHEN 'Footwear' THEN 3.5
    WHEN 'Accessories' THEN 4.1
    WHEN 'Outerwear' THEN 4.3
END
WHERE category IN ('Clothing', 'Footwear', 'Accessories', 'Outerwear');
SET SQL_SAFE_UPDATES = 1;

-- Q31. Which customers give the lowest average ratings?
SELECT customer_id, ROUND(AVG(review_rating),2) AS lowest_avg_rating
FROM t1
GROUP BY  1
ORDER BY 2;

-- Q32. Which customers are “New”, “Returning”, or “Loyal” based on purchase count?
SELECT customer_id, previous_purchases,
CASE 
	WHEN previous_purchases = 1 THEN 'New'
           WHEN previous_purchases BETWEEN 2 AND 5 THEN 'Returning'
           ELSE 'Loyal'
	END AS customer_type
FROM t1;

-- Q33. Which customers are high-value but low-frequency buyers?
SELECT customer_id, SUM(purchase_amount) AS total_spent, previous_purchases AS total_orders
FROM t1
GROUP BY customer_id, previous_purchases
HAVING SUM(purchase_amount) > 90 AND previous_purchases <= 2
ORDER BY total_spent DESC;

-- Q34. Which customers are low-value but high-frequency buyers?
SELECT customer_id, SUM(purchase_amount) AS total_spent, previous_purchases AS total_orders
FROM t1
GROUP BY customer_id, previous_purchases
HAVING SUM(purchase_amount) <= 30 AND previous_purchases >10
ORDER BY total_spent DESC;

-- Q35. Which customers are discount-sensitive but profitable?
SELECT customer_id, SUM(purchase_amount) AS total_spent,
       AVG(CASE WHEN discount_applied='Yes' THEN 1 ELSE 0 END) AS discount_ratio
FROM t1
GROUP BY customer_id
HAVING AVG(CASE WHEN discount_applied='Yes' THEN 1 ELSE 0 END) > 0.7
   AND SUM(purchase_amount) > 30
ORDER BY total_spent DESC;
SELECT customer_id
FROM t1
GROUP BY customer_id
HAVING COUNT(DISTINCT category) > 1;

-- Q36. Which customers switch categories between purchases?
SELECT customer_id
FROM t1
GROUP BY customer_id
HAVING COUNT(DISTINCT category) > 1;

-- Q37. Which customers repeatedly buy the same product?
SELECT customer_id, item_purchased, COUNT(*) AS repeat_count
FROM t1
GROUP BY customer_id, item_purchased
HAVING COUNT(*) > 1
ORDER BY repeat_count DESC;

-- Q38. Which customers repeatedly buy the same category?
SELECT customer_id, category, COUNT(*) AS repeat_count
FROM t1
GROUP BY customer_id, category
HAVING COUNT(*) > 1
ORDER BY repeat_count DESC;

-- Q39. Which customers buy across multiple seasons?
SELECT customer_id, COUNT(DISTINCT season) AS seasons_count
FROM t1
GROUP BY customer_id
HAVING COUNT(DISTINCT season) > 1
ORDER BY seasons_count DESC;

-- Q40. Which customers prefer specific shipping types?
SELECT customer_id, shipping_type, COUNT(*) AS type_count
FROM t1
GROUP BY customer_id, shipping_type
ORDER BY customer_id, type_count DESC;

-- Q41. Which products generate the most revenue?
SELECT  item_purchased, SUM(purchase_amount) AS highest_revene_product
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q42. Which products generate the least revenue?
SELECT  item_purchased, SUM(purchase_amount) AS lowest_revene_product
FROM t1
GROUP BY 1
ORDER BY 2;

-- Q43. Which products have the highest number of unique customers?
SELECT item_purchased, count( DISTINCT customer_id) AS highest_unique_customers
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q44. Which products have the highest discount usage?
SELECT item_purchased, count(discount_applied) AS highest_discount_usage
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q45. Which products have the lowest discount usage?
SELECT item_purchased, count(discount_applied) AS lowest_discount_usage
FROM t1
GROUP BY 1
ORDER BY 2;

-- Q46. Which products are most popular among male customers?
SELECT gender,item_purchased, COUNT(*) AS purchase_count
FROM t1
WHERE gender = 'Male'
GROUP BY 2
ORDER BY 3 DESC;

-- Q47. Which products are most popular among female customers?
SELECT gender,item_purchased, COUNT(*) AS purchase_count
FROM t1
WHERE gender = 'Female'
GROUP BY 2
ORDER BY 3 DESC;

-- Q48. Which products are most popular among each age group?
SELECT age_group, item_purchased, purchase_count
FROM (
    SELECT 
        age_group,
        item_purchased,
        COUNT(*) AS purchase_count,
        RANK() OVER (PARTITION BY age_group ORDER BY COUNT(*) DESC) AS rnk
    FROM t1
    GROUP BY age_group, item_purchased
) sub
WHERE rnk = 1;

-- Q49. Which products are most popular in each location?
SELECT location, item_purchased, purchase_count
FROM (
    SELECT 
        location,
        item_purchased,
        COUNT(*) AS purchase_count,
        RANK() OVER (PARTITION BY location ORDER BY COUNT(*) DESC) AS rnk
    FROM t1
    GROUP BY location, item_purchased
) sub
WHERE rnk = 1;

-- Q50. Which products are most popular in each season?
SELECT season, item_purchased, purchase_count
FROM (
    SELECT 
        season,
        item_purchased,
        COUNT(*) AS purchase_count,
        RANK() OVER (PARTITION BY season ORDER BY COUNT(*) DESC) AS rnk
    FROM t1
    GROUP BY season, item_purchased
) sub
WHERE rnk = 1;

-- Q51. Which categories have the highest discount usage?
SELECT category, COUNT(*) AS discount_usage
FROM t1
WHERE discount_applied = 'Yes'
GROUP BY category
ORDER BY discount_usage DESC;

-- Q52. Which categories have the lowest discount usage?
SELECT category, COUNT(*) AS discount_count
FROM t1
WHERE discount_applied = 'Yes'
GROUP BY category
ORDER BY discount_count ASC;

-- Q53. Which categories have the highest number of unique customers?
SELECT category, COUNT( DISTINCT customer_id) AS unique_customers
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q54. Which categories have the highest average purchase amount?
SELECT category, AVG(purchase_amount) AS average_purchase_amount
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q55. Which categories have the lowest average purchase amount?
SELECT category, AVG(purchase_amount) AS average_purchase_amount
FROM t1
GROUP BY 1
ORDER BY 2;

-- Q56. Which categories have the highest average rating?
SELECT category,ROUND( AVG(review_rating),2 )AS average_rating
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q57. Which categories have the lowest average rating?
SELECT category,ROUND( AVG(review_rating),2 )AS average_rating
FROM t1
GROUP BY 1
ORDER BY 2;

-- Q58. Which categories are most popular among each gender?
SELECT gender, category, COUNT(*) AS category_count
FROM t1
GROUP BY gender, category
ORDER BY gender, category_count DESC;

-- Q59. Which categories are most popular among each age group?
SELECT age_group, category, COUNT(*) AS category_count
FROM t1
GROUP BY age_group, category
ORDER BY age_group, category_count DESC;

-- Q60. Which categories are most popular in each location?
SELECT location, category, COUNT(*) AS category_count
FROM t1
GROUP BY location, category
ORDER BY location, category_count DESC;

-- Q61. What percentage of orders used discounts?
SELECT 
    ROUND(100.0 * SUM(CASE WHEN discount_applied='yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS discount_percentage
FROM t1;

-- Q62. What percentage of revenue comes from discounted orders?
SELECT 
    ROUND(100.0 * SUM(CASE WHEN discount_applied='yes' THEN purchase_amount ELSE 0 END) / SUM(purchase_amount), 2) AS discount_revenue_percentage
FROM t1;

-- Q63. Which seasons have the highest discount usage?
SELECT season, COUNT(*) AS discount_count
FROM t1
WHERE discount_applied='yes'
GROUP BY 1
ORDER BY 2 DESC;

-- Q64. Which locations use discounts the most?
SELECT location, COUNT(*) AS discount_count
FROM t1
WHERE discount_applied='yes'
GROUP BY 1
ORDER BY 2 DESC;

-- Q65. Which genders use discounts the most?
SELECT gender, COUNT(*) AS discount_count
FROM t1
WHERE discount_applied='yes'
GROUP BY 1
ORDER BY 2 DESC;

-- Q66. Which age groups use discounts the most?
SELECT age_group, COUNT(*) AS discount_count
FROM t1
WHERE discount_applied='yes'
GROUP BY 1
ORDER BY 2 DESC;

-- Q67. Do discounted orders have lower or higher average ratings?
SELECT discount_applied, ROUND(AVG(review_rating), 2) AS avg_rating
FROM t1
GROUP BY 1;

-- Q68. Do discounted orders have lower or higher purchase amounts?
SELECT discount_applied, ROUND(AVG(purchase_amount), 2) AS avg_purchase
FROM t1
GROUP BY 1;

-- Q69. Do subscribed customers spend more than unsubscribed customers?
SELECT subscription_status, 
       ROUND(AVG(purchase_amount), 2) AS avg_spent
FROM t1
GROUP BY 1;

-- Q70. Do subscribed customers buy more frequently?
SELECT subscription_status, COUNT(*) AS total_orders
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q71. Which subscription status gives the highest ratings?
SELECT subscription_status, MAX(review_rating) AS highest_rating
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q72. Which shipping type is used the most?
SELECT shipping_type, COUNT(*) AS most_used_shipping_type
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q73. Which shipping type generates the most revenue?
SELECT shipping_type, SUM(purchase_amount) AS most_revenue
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q74. Which shipping type has the highest average purchase amount?
SELECT shipping_type, ROUND(AVG(purchase_amount),2) AS avg_purchase_amt
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q75. Which shipping type has the highest average rating?
SELECT shipping_type, ROUND(AVG(review_rating),2) AS avg_rating
FROM t1
GROUP BY shipping_type
ORDER BY avg_rating DESC;

-- Q76. Which seasons have the highest average purchase amount?
SELECT season, ROUND(AVG(purchase_amount),2)
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q77. Which seasons have the highest average rating?
SELECT season, ROUND(AVG(review_rating),2)
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q78. Which seasons have the highest discount usage?
SELECT season, COUNT(*) AS discount_usage
FROM t1
WHERE discount_applied = 'Yes' or 'No'
GROUP BY season
ORDER BY discount_usage DESC;

-- Q79. Which seasons have the highest number of unique customers?
SELECT season, COUNT(DISTINCT customer_id)
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q80. Which seasons have the highest number of unique products purchased?
SELECT season, COUNT(DISTINCT item_purchased)
FROM t1
GROUP BY 1
ORDER BY 2 DESC;

-- Q81. What are the top 3 products in each category using ranking?
SELECT category, item_purchased, total_sales
FROM (
    SELECT category,
           item_purchased,
           COUNT(*) AS total_sales,
           RANK() OVER (PARTITION BY category ORDER BY COUNT(*) DESC) AS rnk
    FROM t1
    GROUP BY 1,2
) ranked
WHERE rnk <= 3;

-- Q82. What are the top 3 products in each season using ranking?
SELECT season, item_purchased, total_sales
FROM (
        SELECT season, 
               item_purchased,
               COUNT(*) AS total_sales,
               RANK() OVER (PARTITION BY season ORDER BY COUNT(*) DESC) AS rnk
        FROM t1
        GROUP BY 1, 2
     ) AS ranked
WHERE rnk <= 3;

-- Q83. What are the top 3 products in each location using ranking?
SELECT location, item_purchased, total_sales
FROM (
        SELECT location, 
               item_purchased,
               COUNT(*) AS total_sales,
               RANK() OVER (PARTITION BY location ORDER BY COUNT(*) DESC) AS rnk
        FROM t1
        GROUP BY 1, 2
     ) AS ranked
WHERE rnk <= 3;

-- Q84. What are the top 3 categories for each gender using ranking?
SELECT gender, category, total_sales
FROM (
        SELECT gender, 
               category,
               COUNT(*) AS total_sales,
               RANK() OVER (PARTITION BY gender ORDER BY COUNT(*) DESC) AS rnk
        FROM t1
        GROUP BY 1, 2
     ) AS ranked
WHERE rnk <= 3;

-- Q85. What are the top 3 categories for each age group using ranking?
SELECT age_group, category, total_sales
FROM (
        SELECT age_group, 
               category,
               COUNT(*) AS total_sales,
               RANK() OVER (PARTITION BY age_group ORDER BY COUNT(*) DESC) AS rnk
        FROM t1
        GROUP BY 1, 2
     ) AS ranked
WHERE rnk <= 3;

-- Q86. What is the revenue rank of each customer?
SELECT customer_id,
       total_revenue,
       RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM (
        SELECT customer_id,
               SUM(purchase_amount) AS total_revenue
        FROM t1
        GROUP BY customer_id
     ) AS customer_revenue;
     
-- Q87. What is the purchase frequency rank of each customer?
SELECT customer_id,
       purchase_count,
       RANK() OVER (ORDER BY purchase_count DESC) AS frequency_rank
FROM (
        SELECT customer_id,
               COUNT(*) AS purchase_count
        FROM t1
        GROUP BY customer_id
     ) AS customer_frequency;
     
-- Q88. What is the revenue rank of each product?
SELECT item_purchased,
       total_revenue,
       RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM (
        SELECT item_purchased,
               SUM(purchase_amount) AS total_revenue
        FROM t1
        GROUP BY item_purchased
     ) AS product_revenue;
     
-- Q89. What is the revenue rank of each category?
SELECT category,
       total_revenue,
       RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM (
        SELECT category,
               SUM(purchase_amount) AS total_revenue
        FROM t1
        GROUP BY category
     ) AS category_revenue;
     
-- Q90. What is the average purchase amount per customer compared to the overall average?
SELECT customer_id,
       AVG(purchase_amount) AS customer_avg_purchase,
       AVG(AVG(purchase_amount)) OVER () AS overall_avg_purchase
FROM t1
GROUP BY customer_id;

-- Q91. Which product pairs are frequently bought together (self-join)?
SELECT 
    a.item_purchased AS product_1,
    b.item_purchased AS product_2,
    COUNT(*) AS times_bought_together
FROM t1 a
JOIN t1 b
  ON a.customer_id = b.customer_id
 AND a.item_purchased < b.item_purchased
GROUP BY a.item_purchased, b.item_purchased
ORDER BY times_bought_together DESC;

-- Q92. Which customers bought the same product as other customers (self-join)?
SELECT 
    a.customer_id AS customer_1,
    b.customer_id AS customer_2,
    a.item_purchased
FROM t1 a
JOIN t1 b
  ON a.item_purchased = b.item_purchased
 AND a.customer_id < b.customer_id
ORDER BY a.item_purchased;

-- Q93. Which customers bought the same category as other customers (self-join)?
SELECT 
    a.customer_id AS customer_1,
    b.customer_id AS customer_2,
    a.category
FROM t1 a
JOIN t1 b
  ON a.category = b.category
 AND a.customer_id < b.customer_id
GROUP BY a.customer_id, b.customer_id, a.category;

-- Q94. Which customers share similar buying patterns (same color/size)?
SELECT 
    a.customer_id AS customer_1,
    b.customer_id AS customer_2,
    a.color,
    a.size,
    COUNT(*) AS similar_purchases
FROM t1 a
JOIN t1 b
  ON a.color = b.color
 AND a.size = b.size
 AND a.customer_id < b.customer_id
GROUP BY a.customer_id, b.customer_id, a.color, a.size
ORDER BY similar_purchases DESC;

-- Q95. Which customers have overlapping purchase behavior across seasons?
SELECT 
    a.customer_id AS customer_1,
    b.customer_id AS customer_2,
    a.season,
    COUNT(*) AS shared_season_purchases
FROM t1 a
JOIN t1 b
  ON a.season = b.season
 AND a.customer_id < b.customer_id
GROUP BY a.customer_id, b.customer_id, a.season
ORDER BY shared_season_purchases DESC;
