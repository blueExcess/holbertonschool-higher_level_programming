-- 15. Count number of scores that are the same
-- display: score -> number of instances
SELECT score, COUNT(score) AS number
FROM second_table GROUP BY score DESC;
