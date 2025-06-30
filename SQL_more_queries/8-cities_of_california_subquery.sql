-- @block
USE `hbtn_0d_usa`;
SELECT cities.id, cities.state_id, cities.name
FROM cities, states
WHERE cities.state_id = states.id;