#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        cursor = db.cursor()
        cursor.execute("""
            SELECT cities.name FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            WHERE CAST(states.name AS BINARY) = %s
            ORDER BY cities.id;
        """, [sys.argv[4]])
        records = cursor.fetchall()
        print(", ".join(map(lambda x: x[0], records)))
        db.close()
