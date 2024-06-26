#!/usr/bin/python3
"""Lists all cities of a specific state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') " \
            "FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s " \
            "ORDER BY cities.id"

    cur.execute(query, (sys.argv[4],))

    result = cur.fetchone()

    if result[0] is not None:
        print(result[0])

    cur.close()
    db.close()
