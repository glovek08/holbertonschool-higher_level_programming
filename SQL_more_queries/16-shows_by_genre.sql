-- @block
USE `hbtn_0d_usa`;
SELECT id, cities.id AS state_id, name
FROM `cities` ORDER BY cities.id DESC;