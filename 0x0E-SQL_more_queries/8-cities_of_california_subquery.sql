--lists all the cities of california that can be found in hbtn_0d_usa
SELECT id, name FROM cities
WHERE name=(SELECT id FROM states
	WHERE name="California")
ORDER BY cities.id;
