--  Cities of California
SELECT id, name
FROM cities
WHERE name IN state_id = "California"
ORDER BY id ASC;