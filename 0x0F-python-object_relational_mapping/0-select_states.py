#!/usr/bin/python3

"""
script to list all states from db hbtn_0e_usa
takes 3 args mysql username, mysql passwd, db name
"""


if __name__ == "__main__":
    import sys
    from MySQLdb import connect

    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    conn = connect(host="localhost",
                   port=3306,
                   user=u,
                   passwd=p,
                   db=d,
                   charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
