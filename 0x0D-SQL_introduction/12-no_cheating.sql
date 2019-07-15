-- 12. Update info
-- Only use name for bob, not id.
UPDATE second_table
SET score = 10
WHERE second_table.name = "Bob";
