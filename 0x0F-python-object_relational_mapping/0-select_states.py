#!/usr/bin/python3
# script to connect to mysql database in python


from sys import argv
import MySQLdb


if __name__ == "__main__":
    username, password, database = argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    querry = cur.fetchall()
    for row in querry:
        print(row)

    cur.close()
    db.close()
