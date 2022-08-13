/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?


-- members, menu, sales

Select * from dannys_diner.menu m;

select * from dannys_diner.members m;

select * from dannys_diner.sales s;

--- Q1: What is the total amount each customer spent at the restaurant?

select s.customer_id, sum(m.price) as amt_spend
from dannys_diner.sales s
inner join dannys_diner.menu m 
	on s.product_id  = m.product_id  
group by 1;


--- Q2: How many days has each customer visited the restaurant?

select s.customer_id, count(distinct s.order_date) as cnt_days
from dannys_diner.sales s 
group by 1
order by 1 asc 

--- Q3: What was the first item from the menu purchased by each customer? 


SELECT DISTINCT s.customer_id, m.product_name
FROM (
	SELECT  s.customer_id, 
			s.order_date, 
			s.product_id, 
			dense_rank() OVER(PARTITION BY s.customer_id ORDER BY s.order_date asc) AS order_seq
	FROM dannys_diner.sales s
) s
INNER JOIN dannys_diner.menu m
	ON s.product_id = m.product_id
WHERE 1=1
AND s.order_seq = 1

--- Q4: What is the most purchased item on the menu and how many times was it purchased by all customers?

SELECT m.product_name, count(s.order_date) AS orders
FROM dannys_diner.sales s
JOIN dannys_diner.menu m ON s.product_id = m.product_id
GROUP BY 1
ORDER BY orders DESC
LIMIT 1

--- Q5: Which item was the most popular for each customer?

SELECT  s.customer_id, s.product_name, s.orders
FROM (
	SELECT s.customer_id, m.product_name, count(s.order_date) AS orders,
	dense_rank() over(PARTITION BY s.customer_id ORDER BY count(s.order_date) desc) AS order_rank
	FROM dannys_diner.sales s
	JOIN dannys_diner.menu m
		ON s.product_id = m.product_id
	GROUP BY 1,2
) s
WHERE 1=1
AND order_rank = 1

--- Q6: Which item was purchased first by the customer after they became a member?

WITH s AS (
	SELECT  s.customer_id, s.order_date, mem.join_date, m.product_name,
			dense_rank() over(PARTITION BY s.customer_id ORDER BY s.order_date asc) AS order_seq
	FROM dannys_diner.sales s
	JOIN dannys_diner.members mem
		ON s.customer_id = mem.customer_id
	JOIN dannys_diner.menu m
		ON s.product_id = m.product_id
	WHERE 1=1
	AND s.order_date >= mem.join_date
) 
SELECT s.customer_id, s.order_date, s.join_date, s.product_name
FROM s
WHERE 1=1
AND s.order_seq = 1


--- Q7: Which item was purchased just before the customer became a member?

WITH s AS (
	SELECT  s.customer_id, s.order_date, mem.join_date, m.product_name,
			dense_rank() over(PARTITION BY s.customer_id ORDER BY s.order_date desc) AS order_seq
	FROM dannys_diner.sales s
	JOIN dannys_diner.members mem
		ON s.customer_id = mem.customer_id
	JOIN dannys_diner.menu m
		ON s.product_id = m.product_id
	WHERE 1=1
	AND s.order_date < mem.join_date
) 
SELECT s.customer_id, s.order_date, s.join_date, s.product_name
FROM s
WHERE 1=1
AND s.order_seq = 1

--- Q8: What is the total items and amount spent for each member before they became a member?


SELECT  s.customer_id, count(DISTINCT s.product_id) AS unique_items, sum(m.price) AS total_spend			
FROM dannys_diner.sales s
JOIN dannys_diner.members mem
	ON s.customer_id = mem.customer_id
JOIN dannys_diner.menu m
	ON s.product_id = m.product_id
WHERE 1=1
AND s.order_date < mem.join_date
GROUP BY 1


--- Q9: If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?

--- Scenario 1: only counting customers who joined and their transactions after joining
SELECT  s.customer_id, 
		sum(CASE WHEN m.product_name = 'sushi' THEN m.price*20 ELSE m.price*10 END) AS total_points			
FROM dannys_diner.sales s
JOIN dannys_diner.members mem
	ON s.customer_id = mem.customer_id
JOIN dannys_diner.menu m
	ON s.product_id = m.product_id
WHERE 1=1
AND s.order_date >= mem.join_date
GROUP BY 1

--- Scenario 2: assuming all customers are existing members
SELECT  s.customer_id, 
		sum(CASE WHEN m.product_name = 'sushi' THEN m.price*20 ELSE m.price*10 END) AS total_points			
FROM dannys_diner.sales s
JOIN dannys_diner.menu m
	ON s.product_id = m.product_id
WHERE 1=1
GROUP BY 1


--- Q10: In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?



