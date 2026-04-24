-- Top Batsmen
SELECT batsman, SUM(batsman_runs) AS total_runs
FROM ipl_data
GROUP BY batsman
ORDER BY total_runs DESC
LIMIT 10;

-- Strike Rate
SELECT batsman,
SUM(batsman_runs)/COUNT(ball)*100 AS strike_rate
FROM ipl_data
GROUP BY batsman
HAVING COUNT(ball) > 500
ORDER BY strike_rate DESC;

-- Team Wins
SELECT winner, COUNT(*) as wins
FROM ipl_data
WHERE winner != 'No Result'
GROUP BY winner
ORDER BY wins DESC;
