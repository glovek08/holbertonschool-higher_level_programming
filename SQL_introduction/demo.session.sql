-- @block
SELECT COUNT(id) AS total_users FROM users;
-- @block
SELECT * FROM users;
-- @block
SELECT * FROM products
-- @block
SELECT * FROM users JOIN products;
-- @block
SELECT * FROM products JOIN users ON products.created_by = users.id
WHERE users.name = 'Bob'
-- @block
SELECT * FROM products INNER JOIN users;
-- @block
SELECT products.*, users.*
FROM products
JOIN users ON products.created_by = users.id;

-- @block
INSERT INTO products (name, price, created_by) VALUES
('Laptop', 1200, 1),
('Smartphone', 800, 2),
('Headphones', 150, 1),
('Monitor', 300, 3),
('Keyboard', 50, 2);