-- 5. Unique ID
-- creates the table unique_id with a unique id, default value 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
