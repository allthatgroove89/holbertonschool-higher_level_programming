#!/usr/bin/python3
"""script that takes an argument and displays all values in the states table"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (state_name_searched,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
