-- @block
DELETE FROM `second_table`
WHERE `id` IN (
    SELECT `id` FROM (
        SELECT `id` FROM `second_table` WHERE `score` <= 5
    ) AS temp_ids
);