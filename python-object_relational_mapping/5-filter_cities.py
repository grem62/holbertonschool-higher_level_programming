#!/usr/bin/python3
"""Lists all states  starting with 'N' from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()

    cur.execute(

            "SELECT  cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE %s\
            ORDER BY cities.id ASC", (sys.argv[4],))

    cities = cur.fetchall()

    for index in cities:

        resultat = ", ".join(city[0] for city in cities)
        print(resultat)

    cur.close()
    db.close()
