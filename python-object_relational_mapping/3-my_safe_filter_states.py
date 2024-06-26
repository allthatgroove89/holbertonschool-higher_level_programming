#!/usr/bin/python3
""" This script is safe from SQL injections """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (argv[4],))
    # Fetch the first row from the result set
    rows = cursor.fetchall()
    # If a row was fetched, print it
    for row in rows:
        print(row)
    # Close the cursor and the database connection
    cursor.close()
    db.close()
