#!/usr/bin/python3
# list all matches to given argument (fourth arg)


from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, database, state = argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'".format(state))

    querry = cur.fetchall()
    for row in querry:
        print(row)

    cur.close()
    db.close()
