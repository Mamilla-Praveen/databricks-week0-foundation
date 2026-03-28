CREATE TABLE customers1 (
    customer_id INT,
    customer_name STRING,
    city STRING,
    age INT
);

INSERT INTO customers1 VALUES
(1, 'Ravi', 'Hyderabad', 25),
(2, 'Sita', 'Chennai', 32),
(3, 'Arun', 'Hyderabad', 28);

SELECT * FROM customers1;

SELECT * 
FROM customers1
WHERE city = 'Chennai';


SELECT * 
FROM customers1
WHERE age > 25;


SELECT customer_name, city 
FROM customers1;


SELECT city, COUNT(*) AS total_customers
FROM customers1
GROUP BY city;