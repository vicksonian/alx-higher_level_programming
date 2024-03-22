#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa, SQL injection free.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query with parameters
    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query with parameters
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    if result:
        print(result)

    # Close cursor and database connection
    cursor.close()
    db.close()
