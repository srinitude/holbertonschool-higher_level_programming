-- Get score and counts of those scores
SELECT score, COUNT(score) AS number
FROM second_table
ORDER BY score DESC;
