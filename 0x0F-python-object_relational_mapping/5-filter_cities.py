#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa, SQL injection free.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    cursor = db.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4], ))

    cities = cursor.fetchall()

    idx = 0
    for city in cities:
        if idx != 0:
            print(", ", end="")
        print("%s" % city, end="")
        idx += 1
    print("")

    cursor.close()
    db.close()
