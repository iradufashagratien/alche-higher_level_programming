-- 8. Cities of California
-- lists all cities of California, sorted by id, using a subquery (no JOIN)
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
