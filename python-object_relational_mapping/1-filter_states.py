#!/usr/bin/python3
"""Lists all states  starting with 'N' from the database hbtn_0e_0_usa"""
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
            "SELECT * FROM states \
            WHERE name LIKE 'N%' \
            ORDER BY states.id ASC;")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
