#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

# Create a cursor object
cur = db.cursor()

# Execute the query to retrieve all states from the database
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows and print them
for row in cur.fetchall():
    print(row)

# Close the cursor and database connection
cur.close()
db.close()
