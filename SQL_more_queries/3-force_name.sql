-- 3. Always a name
-- creates the table force_name, does not fail if it already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
