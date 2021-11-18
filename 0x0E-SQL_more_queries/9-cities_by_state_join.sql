-- lists all cities contained in the database hbtn_0d_usa
SELECT id, `cities`.`name`, `cities`.`name`
FROM `cities`
INNER JOIN `states`
ORDER BY `cities`.`id`;
