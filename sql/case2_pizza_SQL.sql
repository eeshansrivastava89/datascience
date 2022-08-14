/*

Source: https://8weeksqlchallenge.com/case-study-2/ 

Section 1: 

A. Pizza Metrics
How many pizzas were ordered?
How many unique customer orders were made?
How many successful orders were delivered by each runner?
How many of each type of pizza was delivered?
How many Vegetarian and Meatlovers were ordered by each customer?
What was the maximum number of pizzas delivered in a single order?
For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
How many pizzas were delivered that had both exclusions and extras?
What was the total volume of pizzas ordered for each hour of the day?
What was the volume of orders for each day of the week?

*/

-- Section 1: Pizza Metrics

-- Q1: How many pizzas were ordered?

SELECT count(order_id) AS total_pizzas_ordered
FROM pizza_runner.customer_orders


-- Q2: How many unique customer orders were made?

SELECT count(DISTINCT order_id) AS total_unique_orders
FROM pizza_runner.customer_orders

-- Q3: How many successful orders were delivered by each runner?

SELECT ro.runner_id, count(DISTINCT co.order_id)
FROM pizza_runner.customer_orders co
JOIN pizza_runner.runner_orders ro
	ON co.order_id = ro.order_id
WHERE 1=1
AND (ro.cancellation NOT LIKE ('%Cancellation%') OR ro.cancellation IS NULL)
GROUP BY 1


-- Q4: How many of each type of pizza was delivered?

SELECT pn.pizza_name, count(co.pizza_id) AS pizza_count
FROM pizza_runner.customer_orders co
JOIN pizza_runner.runner_orders ro
	ON co.order_id = ro.order_id
JOIN pizza_runner.pizza_names pn
	ON co.pizza_id = pn.pizza_id
WHERE 1=1
AND (ro.cancellation NOT LIKE ('%Cancellation%') OR ro.cancellation IS NULL)
GROUP BY 1

-- Q5: How many Vegetarian and Meatlovers were ordered by each customer?

SELECT  co.customer_id, 
		count(CASE WHEN pn.pizza_name = 'Vegetarian' THEN co.pizza_id ELSE NULL END) AS veg_count,
		count(CASE WHEN pn.pizza_name = 'Meatlovers' THEN co.pizza_id ELSE NULL END) AS meat_count
FROM pizza_runner.customer_orders co
JOIN pizza_runner.pizza_names pn
	ON co.pizza_id = pn.pizza_id
WHERE 1=1
GROUP BY 1
ORDER BY 1 asc

-- Q6: What was the maximum number of pizzas delivered in a single order?



-- Q7: For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
-- Q8: How many pizzas were delivered that had both exclusions and extras?
-- Q9: What was the total volume of pizzas ordered for each hour of the day?
-- Q10: What was the volume of orders for each day of the week?