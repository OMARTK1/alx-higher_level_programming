#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Delete duplicate entries using a subquery
    cur.execute("""DELETE FROM states WHERE id NOT IN
                (SELECT * FROM (SELECT MIN(id)
                FROM states GROUP BY name) as x)""")

    # Fetch and print distinct state entries
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
