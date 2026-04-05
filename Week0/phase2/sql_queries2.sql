
CREATE TABLE customers2 (
    customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders2 (
    order_id INT,
    customer_id INT,
    amount INT
);


INSERT INTO customers2 VALUES
(1, 'Ravi', 'Hyderabad'),
(2, 'Sita', 'Chennai'),
(3, 'Arun', 'Bangalore'),
(4, 'Priya', 'Hyderabad'),
(5, 'Kiran', 'Mumbai');

INSERT INTO orders2 VALUES
(101, 1, 500),
(102, 1, 300),
(103, 2, 700),
(104, 3, 200),
(105, 3, 400),
(106, 4, 1000);


SELECT customer_id, SUM(amount) AS total_amount
FROM orders2
GROUP BY customer_id;




SELECT customer_id, SUM(amount) AS total_amount
FROM orders2
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 3;



SELECT c.customer_id, c.name
FROM customers2 c
LEFT JOIN orders2 o
ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;


SELECT c.city, SUM(o.amount) AS total_revenue
FROM customers2 c
JOIN orders2 o
ON c.customer_id = o.customer_id
GROUP BY c.city;



SELECT customer_id, AVG(amount) AS avg_amount
FROM orders2
GROUP BY customer_id;

SELECT customer_id, COUNT(*) AS order_count
FROM orders2
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT customer_id, SUM(amount) AS total_amount
FROM orders2
GROUP BY customer_id
ORDER BY total_amount DESC;


