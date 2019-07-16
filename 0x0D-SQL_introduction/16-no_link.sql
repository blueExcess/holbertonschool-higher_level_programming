-- 16. list all records with rules
-- no NULL names, score -> name, DESC score
SELECT `score`, `name` FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
