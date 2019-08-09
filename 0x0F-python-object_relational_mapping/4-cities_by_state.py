#!/usr/bin/python3
# Make #2 safe from sql injection


from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, database = argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")

    querry = cur.fetchall()
    for row in querry:
        print(row)

    cur.close()
    db.close()
