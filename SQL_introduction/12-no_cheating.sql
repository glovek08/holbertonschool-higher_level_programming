-- @block
UPDATE `second_table`
SET `score` = 10
WHERE CAST(`name` AS BINARY) = BINARY 'Bob';
