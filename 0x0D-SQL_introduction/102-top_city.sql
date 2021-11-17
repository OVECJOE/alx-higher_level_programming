-- Displays the 3 cities with the highest temperatures btw July & August
SELECT city, AVG(value) FROM avg_temp
FROM temperatures
WHERE `month` = 7 OR `month` = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
