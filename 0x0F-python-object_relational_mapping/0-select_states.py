#!/usr/bin/python3
'''
lists all states from the database hbtn_0e_0_usa
'''
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for state in query_rows:
      print("({}, '{}')".format(state.id, state.name))
    cur.close()
    conn.close()
