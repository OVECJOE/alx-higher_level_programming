-- displays the average temperature (Fahrenheit) by city ordered
-- by temp (descending)
SELECT city, AVG(*) AS avg_temp
FROM temperatures
GROUP BY COUNT(value)
ORDER BY value DESC;
