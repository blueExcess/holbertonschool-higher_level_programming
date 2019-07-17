-- 5. Create new table with unique id
-- ID must be unique
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT "1" UNIQUE,
name VARCHAR(256));
