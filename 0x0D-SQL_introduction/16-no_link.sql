-- Say my name
SELECT score, name FROM second_table
GROUP BY name, score
ORDER BY score DESC;
