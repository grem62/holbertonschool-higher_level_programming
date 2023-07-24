-- number by score
SELECT score, name
FROM second_table
where name IS NOT NULL
ORDER BY score DESC
